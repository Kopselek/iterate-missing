# Iterate Missing Internationalization
iterate-missing-i18n is designed to compare keys in diffrent YAML language files and identify any missing keys in comparison to a base file. The script is intended to help ensure that all language files have the same keys, making it easier to maintain consistency across different language versions of an application.

## Prerequisites
Before using this script, ensure you have the following installed:

Python 3  
ruamel.yaml library, which can be installed using `pip install ruamel.yaml`

## Usage
1. Place the base language file that you want to compare other files against in the same directory as this script. By default, the base file is 'messages.pl.yaml'.
2. Create additional language files for comparison (e.g., 'messages.en.yaml', 'messages.de.yaml', 'messages.es.yaml') in the same directory, or change 57-59 lines to your requirements.
3. Run the script with following command:
```
python main.py
```
4. The script will compare the keys in the base file with each of the additional language files. Any missing keys in the additional files will be displayed in the console.

## Example
Suppose you have the following in your directory:
- messages.pl.yaml (base file)
- messages.en.yaml
- messages.de.yaml
- messages.es.yaml  
Running the script will compare the keys in the base file (messages.pl.yaml) with the keys in the other language files and print out any missing keys in each of the additional files.  

