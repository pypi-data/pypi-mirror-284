from setuptools import setup, find_packages

setup(
    name='gocodeo',
    version='0.0.15',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            # 'gocodeo-generate = gocodeo.generator:generate_tests_cli',
            # 'gocodeo-train = gocodeo.train:start',

            'gocodeo-generate = gocodeo.executable:generate_tests_cli',
            "gocodeo-advanced = gocodeo.executable:advanced",

            # 'gocodeo-generate = gocodeo.demo:generate_tests_cli',
            # "gocodeo-advanced = gocodeo.demo:advanced"

            
            # "gocodeo-generate = gocodeo.python_demo:generate_tests_cli",
            # "gocodeo-advanced = gocodeo.python_demo:advanced"

            #  "gocodeo-generate = gocodeo.generalized:generate_tests_cli",
            # "gocodeo-advanced = gocodeo.generalized:advanced"



        
        ]
    },
    install_requires= ['vertexai',
                       'requests',
                       'google-cloud-aiplatform',
                       'google-auth',
                       'python-dotenv',
                       'google-cloud-storage',
                       'pymongo',
                       
                       ],

    author='GoCodeo AI',
    description='A package to generate unit tests for a file',
    long_description='''\
        gocodeo is a  package that provides a command-line interface (CLI) to generate unit tests for files. 
        To use gocodeo , simply run the command:
        
            gocodeo generate <file_path>
            
        For example:
        
            gocodeo generate C:\\Users\\Sky\\Desktop\\Demo.ts
        
        This will analyze the file specified and generate unit tests based on its contents.
    ''',
    long_description_content_type='text/markdown',
)
