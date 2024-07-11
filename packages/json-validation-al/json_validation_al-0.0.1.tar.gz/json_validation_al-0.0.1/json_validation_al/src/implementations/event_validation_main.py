from event_validation.base import EventValidationBase
import json
from jsonschema import ValidationError, Draft7Validator, FormatChecker
import inspect
import importlib.util


class EventValidation(EventValidationBase):

    def get_validation_schema(self, file_path: str) -> dict:
        """
        Reads a JSON schema from a file and returns it as a dictionary.

        Parameters:
        - file_path (str): The path to the JSON schema file.

        Returns:
        - dict: The JSON schema as a dictionary.

        Raises:
        - FileNotFoundError: If the file does not exist.
        - json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}")
        except Exception as e:
            raise e


    def load_custom_validations(self, file_path: str):
        try:
            spec = importlib.util.spec_from_file_location('custom_validators', file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for name, func in inspect.getmembers(module, inspect.isfunction):
                # Add functions to the custom_checkers dictionary
                custom_checkers = {}
                custom_checkers[name] = func
            return custom_checkers        
        except Exception as e:
            print("Error loading custom validations")
            raise e

    def do_validation(self, event: dict, schema: dict, custom_validation_functions: dict = None) -> tuple:
        """
        Validates an event against a JSON schema.

        Parameters:
        - event (dict): The event to validate.
        - schema (dict): The JSON schema to validate against.

        Returns:
        - tuple: True if the event is valid, False otherwise. Also returns an array of error messages when validation fails.
        """

        messages = []
        format_checker = FormatChecker()
        
        # Add custom validation functions
        if custom_validation_functions:
            for format_name, checker_function in custom_validation_functions.items():

                format_checker.checks(format_name)(checker_function)

        validator = Draft7Validator(schema=schema, format_checker=format_checker)

        errors = sorted(validator.iter_errors(event), key=lambda e: e.path)
        if errors:
            messages = []
            for error in errors:
                message = f"{'.'.join([str(i) for i in error.path])}: {error.message}"
                messages.append(message)
            return False, messages
        else:
            return True, []        