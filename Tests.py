import json
import pandas as pd
from ApiClient import ApiClient

class Tests:
    tests = []

    def __init__(self, api_url, api_key, auto_mode = False):
        self.api_url = api_url
        self.api_key = api_key
        self.auto_mode = auto_mode
        self.results = []

    def run_test(self, method_type, method, template_result, status_code = 200, params = {}):
        print(f"Тестирование метода {method_type} {method}")

        client = ApiClient(self.api_url, self.api_key)
        test = {
            "method_type": method_type,
            "method": method,
            "template_result": template_result,
            "status_code": status_code,
            "params": params
        }
        response = None

        if method_type == 'GET':
            response = client.get(method, params)
        elif method_type == 'POST':
            response = client.post(method, params)
        elif method_type == 'PATCH':
            response = client.patch(method, params)
        elif method_type == 'DELETE':
            response = client.delete(method)
        else:
            response = client.get(method)

        self.check_response(test, response)

        if not self.auto_mode:
            input("Нажмите Enter для продолжения к следующему тесту...")

        return response.text

    def check_response(self, test, response):
        result = {
            'Метод': f'{test['method_type']}: {test['method']}',
            'Параметры запроса': json.dumps(test['params']),
            'Ожидаемый код ответа': test['status_code'],
            'Ожидаемый вид ответа': test['template_result'],
            'Полученный код ответа': response.status_code,
            'Полученный ответ запроса': response.text
        }

        if response.status_code != test['status_code']:
            result['Комментарий'] = f'Неожиданный код ответа {response.status_code}'
        else:
            validate = self.validate_response(response.text, test['template_result'])

            if validate != True:
                result['Комментарий'] = f'Некорректный ответ сервера: {validate}'

        self.results.append(result)

    def validate_response(self, response, template):
        try:
            if template != "int":
                response = json.loads(response)
            
            # print('-----------------------------------------------')
            # print(response, type(response), template)

            if type(template) is list and not isinstance(response, type(template)):
                return ["Ответ не является массивом."]
            elif type(template) is dict and not isinstance(response, type(template)):
                return ["Ответ не является объектом."]
            elif template == "int" and not isinstance(response, int):
                return ["Ответ не является значением типа int."]
            else:
                errors = []

                try:
                    if type(template) is list:
                       response_object = response[0]
                       template_object = template[0]
                    else:
                       response_object = response
                       template_object = template
                except IndexError:
                    return ["Ответ не является объектом."]

                if not isinstance(response_object, dict):
                    return ["Ответ не является объектом."]

                # for key in template_object.keys():
                #     if key not in response_object:
                #         errors.append(f"Поле '{key}' отсутствует в ответе. Ответ не соответствует документации.")

                for key, expected_type in template_object.items():
                    if key not in response_object:
                        errors.append(f"Поле '{key}' отсутствует в ответе. Ответ не соответствует документации.")
                    else:
                        if expected_type == "int" and not isinstance(response_object[key], int) and not (type(response_object[key]) == None):
                            errors.append(f"Поле '{key}' должен быть типа 'int'.")
                        elif expected_type == "string" and not isinstance(response_object[key], str) and not (type(response_object[key]) == None):
                            errors.append(f"Поле '{key}' должен быть типа 'string'.")
                        elif expected_type == "bool" and not isinstance(response_object[key], bool) and not (type(response_object[key]) == None):
                            errors.append(f"Поле '{key}' должен быть типа 'bool'.")
                        elif expected_type == "float" and not isinstance(response_object[key], float) and not (type(response_object[key]) == None):
                            errors.append(f"Поле '{key}' должен быть типа 'float'.")
                        elif isinstance(expected_type, list):
                            if not isinstance(response_object[key], list):
                                errors.append(f"Поле '{key}' должно быть массивом.")
                            for item in response_object[key]:
                                validate = self.validate_response(json.dumps(item), expected_type[0])

                                if validate != True:
                                    errors.append(validate)
                        elif isinstance(expected_type, dict):
                            if not isinstance(response[key], dict):
                                errors.append(f"Поле '{key}' должно быть объектом.")

                            validate = self.validate_response(json.dumps(response[key]), expected_type)

                            if validate != True:
                                errors.append(validate)
                        elif response_object[key] is None:
                            ...
                if errors:
                    return errors
                
                return True
    
        except json.JSONDecodeError:
            print("Ошибка при парсинге JSON.")
            return "Ошибка при парсинге JSON."
    
    def save_report(self, output_file):
        if self.results:
            df = pd.DataFrame(self.results)
            df.to_excel(f"{output_file}.xlsx", index=False)
        else:
            print("No results to save.")
        
    # def add_test(self, method_type, method, template_result, status_code = 200, params = {}):
    #     self.tests.append({
    #         'method_type': method_type,
    #         'method': method,
    #         'template_result': template_result,
    #         'status_code': status_code,
    #         'params': params
    #     })

    # def check_responses(self, test, responses):
    #     result = {
    #         'Метод': f'{test['method_type']}: {test['method']}',
    #         'Параметры запроса': json.dumps(test['params']),
    #         'Ожидаемый код ответа': test['status_code'],
    #         'Ожидаемый вид ответа': test['template_result'],
    #     }

    #     for index, response in enumerate(responses):
    #         api_key_label = f''
    #         result['Полученный код ответа' + api_key_label] = response.status_code
    #         result['Полученный ответ запроса' + api_key_label] = response.text

    #         if response.status_code != test['status_code']:
    #             result['Комментарий' + api_key_label] = f'Неожиданный код ответа {response.status_code}'
    #         else:
    #             validate = self.validate_response(response.text, test['template_result'])
    #             if validate != True:
    #                 result['Комментарий' + api_key_label] = f'Некорректный ответ сервера: {validate}'

    #     self.results.append(result)

    # def run_tests(self, output_file):
    #     for test in self.tests:
    #         responses = []
            
    #         print(f"Тестирование метода {test['method_type']} {test['method']}")

    #         for api_key in self.api_keys:
    #             client = ApiClient(self.api_url, api_key)

    #             if test['method_type'] == 'GET':
    #                 responses.append(client.get(test['method']))
    #             elif test['method_type'] == 'POST':
    #                 responses.append(client.post(test['method'], test['params']))
    #             elif test['method_type'] == 'PATCH':
    #                 responses.append(client.patch(test['method']))
    #             elif test['method_type'] == 'DELETE':
    #                 responses.append(client.delete(test['method']))
    #             else:
    #                 responses.append(client.get(test['method']))

    #         self.check_responses(test, responses)

    #         input("Нажмите Enter для продолжения к следующему тесту...")

    #     self.save_results_to_excel(output_file, self.results)
    #     print(f"Тестирование завершено. Результаты сохранены в '{output_file}.xlsx'.")

    def save_results_to_excel(self, output_file, results):
        if results:
            df = pd.DataFrame(results)
            df.to_excel(f"{output_file}.xlsx", index=False)
        else:
            print("No results to save.")