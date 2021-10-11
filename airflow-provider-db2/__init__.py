def get_provider_info():
    return {
        "package-name": "airflow-provider-db2-custom",
        "name": "DB2 Airflow Provider",
        "description": "A custom DB2 provider to implement a conn type that uses ibm_db library, a workaround to use SECURITYMECHANISM parameter to connect to DB2", # Required
        "hook-class-names": ["db2_provider.hooks.db2_hook.DB2Hook"],
        'connection-types': [
                        {
                            'hook-class-name': 'db2_provider.hooks.db2_hook.DB2Hook',
                            'connection-type': 'DB2',
                        }
                    ],
        "versions": ["0.0.1"]
        }
    }