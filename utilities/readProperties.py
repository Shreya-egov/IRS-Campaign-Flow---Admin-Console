import configparser

class ReadConfig:
    config = configparser.ConfigParser()
    config.read(".//configurations/config.ini")  # Ensure this path is correct

    @staticmethod
    def get_application_url():
        """Retrieve the base URL from the config file."""
        return ReadConfig.config.get('common info', 'baseURL')

    @staticmethod
    def get_username():
        """Retrieve the username from the config file."""
        return ReadConfig.config.get('common info', 'username')

    @staticmethod
    def get_password():
        """Retrieve the password from the config file."""
        return ReadConfig.config.get('common info', 'password')
    
    @staticmethod
    def get_country_name():
        return ReadConfig.config.get('common info', 'country_name')
