# PistolMagazine 🎯
[![PyPI - Version](https://img.shields.io/pypi/v/PistolMagazine)](https://pypi.org/project/PistolMagazine/)


PistolMagazine is a data mocking tool designed to help you generate realistic data for testing and development purposes.

## Features ✨

- **Flexible Data Types** 📊: Supports various data types including integers, floats, strings, timestamps, and more.
- **Custom Providers** 🛠️: Easily create and integrate custom data providers.
  - **Built-in Providers** 🏗️: Provides several built-in providers for common use cases.
- **Random Data Generation** 🎲: Generates realistic random data for testing.
- **Hook Functions** 🪝: Support for hook functions, allowing users to execute custom operations before or after generating mock data. These hooks can be utilized for:
  - **Logging**: Record relevant operations or data before or after data generation.
  - **Starting External Services**: Initiate external services or resources before generating data.
  - **Dynamic Data Modification**: Perform data validation or sanitization before generating mock data.
  - **Sending Data to Message Queues**: Transmit generated data to message queues for integration with other systems.
  - **Data Profiling**: Perform statistical analysis or monitoring post data generation.
- **Data Export** 📤: Supports exporting to CSV, JSON, XML, and MySQL. Can be used in conjunction with hook functions.

## Installation 📦

Install PistolMagazine using pip:

```bash
pip install PistolMagazine
```

## Quick Start 🚀

Here’s a quick example to get you started:

```python
from pistol_magazine import *
from random import choice
from pistol_magazine.hooks.hooks import hook

# Create a custom provider
@provider
class MyProvider:
    def user_status(self):
        return choice(["ACTIVE", "INACTIVE"])
    
    
"""
Define hook functions
pre_generate: Executes operations before generating all data. Suitable for tasks like logging or starting external services.
after_generate: Executes operations after generating each data entry but before final processing. Suitable for tasks like data validation or conditional modifications.
final_generate: Executes operations after generating and processing all data entries. Suitable for final data processing, sending data to message queues, or performing statistical analysis.
"""
@hook('pre_generate', order=1, hook_set='SET1')
def pre_generate_first_hook():
    print("Start Mocking User Data")


@hook('pre_generate', order=2, hook_set='SET1')
def pre_generate_second_hook():
    """
    Perform some preprocessing operations, such as starting external services.
    """


@hook('after_generate', order=1, hook_set="SET1")
def after_generate_first_hook(data):
    data['user_status'] = 'ACTIVE' if data['user_age'] >= 18 else 'INACTIVE'
    return data


@hook('final_generate', order=1, hook_set="SET1")
def final_generate_second_hook(data):
    """
    Suppose there is a function send_to_message_queue(data) to send data to the message queue
    """

# Use the custom provider
class UserInfo(DataMocker):
    create_time: Timestamp = Timestamp(Timestamp.D_TIMEE10, days=2)
    user_name: Str = Str(data_type="name")
    user_email: Str = Str(data_type="email")
    user_age: Int = Int(byte_nums=6, unsigned=True)
    user_status: ProviderField = ProviderField(MyProvider().user_status)
    user_marriage: Bool = Bool()
    user_dict: Dict = Dict(
        {
            "a": Float(left=2, right=4, unsigned=True),
            "b": Timestamp(Timestamp.D_TIMEE10, days=2)
        }
    )
    user_list: List = List(
        [
            Datetime(Datetime.D_FORMAT_YMD_T, weeks=2),
            StrInt(byte_nums=6, unsigned=True)
        ]
    )

data = UserInfo().mock(num_entries=2, as_list=False, to_json=True, hook_set='SET1')
"""
e.g.
{"dda7d976-5094-4395-be92-306e7618ec48": {"create_time": 1718601558, "user_name": "Matthew Burke", "user_email": "aaronbrown@example.org", "user_age": 56, "user_status": "ACTIVE", "user_marriage": true, "user_dict": {"a": 5.1988, "b": 1718523595}, "user_list": ["2024-06-08T14:54:16", "44"]}, "c78f7896-f08c-414e-823b-8f173ab8259b": {"create_time": 1718685343, "user_name": "Dennis Collier", "user_email": "amy02@example.com", "user_age": 30, "user_status": "ACTIVE", "user_marriage": true, "user_dict": {"a": 55.2365, "b": 1718577918}, "user_list": ["2024-06-26T16:40:48", "43"]}}
"""
print(data)

```

If you want more detailed instructions, you can refer to the examples and documentation in the [wiki](https://github.com/miyuki-shirogane/PistolMagazine/wiki).


## Help PistolMagazine

If you find PistolMagazine useful, please ⭐️ Star it at GitHub

[Feature discussions](https://github.com/miyuki-shirogane/PistolMagazine/discussions) and [bug reports](https://github.com/miyuki-shirogane/PistolMagazine/issues) are also welcome!

**Happy Mocking!** 🎉🎉🎉