from collections import namedtuple
import ast
import datetime
import messages
import processors.propertymanager as pm

Mapping = namedtuple('Mapping', ['ref_name', 'returned_name'], defaults=(None, None))

class Properties(dict):

    @staticmethod
    def _escape(string: str) -> str:
        res = string.replace('\\', '\\\\').replace('\r', '\\r').replace('\n', '\\n').replace('"', '\\"')
        return res

    @staticmethod
    def _format_value(key, value, ref=''):

        def parse_formula(formula):
            num_open = 0
            num_close = 0
            parsed = ''
            index = 0
            open = False
            property_name = ''
            while index < len(formula):
                this_char = formula[index]
                next_char = (formula+' ')[index+1]
                if this_char == '{':
                    if next_char == '{':
                        if open:
                            property_name += this_char
                        else:
                            parsed += this_char
                        index += 1
                    else:
                        open = True
                        property_name = ''
                        num_open += 1
                elif this_char == '}':
                    if next_char == '}':
                        if open:
                            property_name += this_char
                        else:
                            parsed += this_char
                        index += 1
                    else:
                        parsed += ref + pm.validate_property(property_name)
                        open = False
                        num_close += 1
                else:
                    if open:
                        property_name += this_char
                    else:
                        parsed += this_char
                index += 1

            ok = (num_open == num_close)
            if num_open == 0:
                parsed = quote + parsed + quote

            return parsed, ok

        def try_date_format(date_format):
            try:
                tested_date = datetime.datetime.strptime(value.replace('/', '-'), date_format).date()
            except:
                tested_date = None
            return tested_date

        def try_dates():
            date1 = try_date_format('%Y-%m-%d')
            date2 = try_date_format('%d-%m-%Y')
            date_found = date1 or date2
            return date_found

        quote = '"'
        escaped_value = Properties._escape(value)
        if len(key.split(':')) == 2:
            # data type defined on header
            given_data_type = key.split(':')[-1]
            try:
                match given_data_type:
                    case 'str':
                        result, ok = parse_formula(escaped_value)
                        if not ok:
                            messages.warning_message(f'{escaped_value} is not valid')
                    case 'int':
                        # Remove any leading zeroes because the literal_eval function does not support them
                        while escaped_value.startswith('0'):
                            escaped_value = escaped_value[1:]
                        result = int(ast.literal_eval(escaped_value))
                        if result != ast.literal_eval(escaped_value):
                            messages.warning_message('Invalid data: ', f'{ast.literal_eval(escaped_value)} is not a valid Integer, {result} used instead')
                    case 'float':
                        result = float(ast.literal_eval(escaped_value))
                    case 'bool':
                        result = ast.literal_eval(escaped_value.capitalize())
                        if str(result) not in ['True', 'False']:
                            messages.error_message('Invalid data: ', f'{ast.literal_eval(escaped_value)} is not a valid boolean so not set')
                            result = ''
                    case 'date':
                        formatted_date = try_dates()
                        if formatted_date:
                            result = 'date("' + str(formatted_date) + '")'
                        else:
                            messages.error_message(f'Invalid data: {value} is not a valid date so value not set')
                            result = ''
                    case _:
                        # Treat unsupported formats as strings
                        result = quote + escaped_value + quote
            except:
                messages.error_message('Invalid data: ', f'{value} is not valid for type {given_data_type} so value not set!')
                result = ''
        else:
            try:
                # Use .capitalize() here to catch incorrectly formatted Booleans (e.g. 'true')
                boolean_check = value.capitalize()
                if boolean_check == 'True' or boolean_check == 'False':
                    data_type = bool
                else:
                    data_type = type(ast.literal_eval(value))
            except:
                # Now see if it's a date
                date1 = try_date_format('%Y-%m-%d')
                date2 = try_date_format('%d-%m-%Y')
                formatted_date = date1 or date2
                data_type = 'date' if formatted_date else 'str'

            if value is None:
                result = 'null'
            else:
                match str(data_type):
                    case 'str':
                        result, ok = parse_formula(escaped_value)
                        if not ok:
                            messages.warning_message(f'{escaped_value} is not valid')
                    case "<class 'int'>":
                        if escaped_value != '0' and escaped_value.startswith('0'):
                            # Has a leading 0, so treat as a string
                            result = quote + escaped_value + quote
                        else:
                            result = int(ast.literal_eval(escaped_value))
                            if result != ast.literal_eval(escaped_value):
                                messages.warning_message('Invalid data: ', f'{ast.literal_eval(escaped_value)} is not a valid Integer, {result} used instead')
                    case "<class 'float'>":
                        result = ast.literal_eval(escaped_value)
                    case "<class 'bool'>":
                        result = ast.literal_eval(escaped_value.capitalize())
                    case "<class 'list'>":
                        result = escaped_value
                    case 'date':
                        formatted_date = try_dates()
                        if formatted_date:
                            result = 'date("' + str(formatted_date) + '")'
                        else:
                            messages.error_message('Invalid data: ', f'{value} is not valid for type {data_type} so value not set')
                            result = ''
                    case _:
                        # Shouldn't get here, but just in case use a string
                        result, ok = parse_formula(escaped_value)
                        if not ok:
                            messages.warning_message(f'{escaped_value} is not valid')

        return result

    def to_str(self, comparison_operator: str = ':', boolean_operator: str = ',', property_ref='', key_ref='') -> str:
        pairs = [f'{key_ref}{key.split(":")[0]}{comparison_operator}{Properties._format_value(key, str(value), property_ref)}' for key, value in self.items()]
        res = boolean_operator.join(pairs)
        return res

    def format(self, property_ref=''):
        # Reformat using identified data types
        pairs = []
        for key, value in self.items():
            pairs.append(f'{key.split(":")[0]}:{Properties._format_value(key, str(value), property_ref)}')
        return '{' + ','.join(pairs) + '}'

    def __str__(self) -> str:
        return self.to_str()
