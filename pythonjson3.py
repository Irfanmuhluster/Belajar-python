'kazoo': {
            'accounts': {
                'jcamp': {
                    'password': 'jcamp',
                    'realm': 'jcamp.kaio.sri',
                    'username': 'jcamp'
                },
                'ofon': {
                    'password': 'ofon',
                    'realm': 'ofon.kaio.sri',
                    'role': 'superduper',
                    'username': 'admin',
                    'devices': [
                        {
                            'number': '021-3971-0000',
                            'password': 'rahasia',
                            'username': 'resepsionis'
                        },
                        {
                            'number': '021-3971-0001',
                            'password': 'rahasia',
                            'username': 'support'
                        },
                        {
                            'number': 1234,
                            'password': 'rahasia',
                            'username': 'dapur'
                        },
                        {
                            'number': 1110,
                            'password': 'rahasia',
                            'username': 'satpam'
                        }
                    ],
                    'numbers': {
                        'conference': '021-3971-0011',
                        'main': '021-3971-0000',
                        'other': [
                            '021-3971-0001',
                            '021-3971-0002'
                        ]
                    },
                }
            },
            'apps': [
                'accounts',
                'acdc',
                'alerts',
                'anonymous_cdrs',
                'dedicated_ips',
                'faxes',
                'global_provisioner',
                'oauth',
                'offnet',
                'pending_notifications',
                'port_requests',
                'ratedeck',
                'services',
                'sip_auth',
                'system_auth',
                'system_config',
                'system_data',
                'system_media',
                'system_schemas',
                'tasks',
                'token_auth',
                'webhooks'
            ],
            'carriers': {
                'tlekom': {
                    'gateways': [
                        {
                            'endpoint_type': 'sip',
                            'port': 5060,
                            'realm': 'fs.sri',
                            'register': False,
                            'server': '192.168.5.92'
                        }
                    ],
                    'rules': [
                        '^.{5,}$'
                    ]
                }
            },
            'config': {
                'number_manager': {
                    'classifiers': {
                        'callcenter1': {
                            'friendly_name': 'PusatLayanan',
                            'pretty_print': '140#',
                            'regex': '^(140)(\\d\\d)$'
                        },
                        'callcenter2': {
                            'friendly_name': 'PusatLayanan',
                            'pretty_print': '1500-###',
                            'regex': '^(1500)(\\d{3})$'
                        },
                        'landline1': {
                            'friendly_name': 'Interlokal',
                            'pretty_print': '0##-####-###',
                            'regex': (
                                '^(?:0|\\+?62)?(?:(61|21|22|24|31)(\\d{3,4})(\\d{3,4}))$'
                            ),
                        },
                        'landline2': {
                            'friendly_name': 'Interlokal',
                            'pretty_print': '0###-###-###',
                            'regex': (
                                '^(?:0|\\+?62)?(?:(?:(?!61|21|22|24|31)([2345679]\\d\\d))(\\d{3})(\\d{3,4}))$'
                            ),
                        },
                        'mobile': {
                            'friendly_name': 'Seluler',
                            'pretty_print': '0###-###-######',
                            'regex': '^(?:0|\\+?62)?(8\\d\\d)(\\d{6,10})$'
                        },
                        'tollfree': {
                            'friendly_name': 'BebasPulsa',
                            'pretty_print': '08##-###-###',
                            'regex': '^(08\\d\\d)(\\d{3})(\\d{3})$'
                        }
                    },
                    'e164_converters': {
                        '^\\+62(\\d{9,12})$': {
                            'prefix': 0
                        }
                    },
                    'reconcile_regex': '^(:?(?:0|\\+?62)?(?:[^1]\\d{6,12}|14\\d{3}|1500\\d{3})|1\\d\\d)$'
                }
            },
            'cookie': 'SAYA_JUGA_JANGAN_DIUBAH',
            'crossbar_apps': [
                'accounts',
                'callflows',
                'fax',
                'numbers',
                'pbxs',
                'voicemails',
                'voip',
                'webhooks'
            ],
            'numbers': {
                'bulk_numbers': {
                    'count': 100,
                    'numbers': [
                        '+62761600XXXX',
                        '0271-162-XXXX',
                        '+62213970XXXX',
                        '021-3971-XXXX',
                        '+62213972XXXX',
                        '+62213973XXXX',
                        '+62223050XXXX',
                        '+62251310XXXX',
                        '+62254320XXXX',
                        '+62231300XXXX',
                        '+62243000XXXX',
                        '+62313000XXXX',
                        '+62361620XXXX'
                    ],
                    'provision': True,
                    'test_call': False
                },
                'did': {
                    'numbers': [
                        '061-62000000',
                        '061-62000001',
                        '061-62000002',
                        '061-62000003',
                        '061-62000004',
                        '061-62000005',
                        '061-62000006',
                        '061-62000007',
                        '061-62000008',
                        '021-39700003',
                        '021-39700004',
                        '021-39700005'
                    ],
                    'provision': True,
                    'test_call': False,
                },
            },
        },