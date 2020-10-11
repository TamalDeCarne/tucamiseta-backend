## [Unrealeased]

## [0.0.1] - 2020-08-10

### Added
- README, changelog, gitignore files

## [0.2.0] - 2020-08-10

### Added
- __init__.py to run the API
- Blueprints/cities.py [Routes for the Table 'municipios']
- models.py [Model of the City Object]
- schemas.py [Schema from the City Model]
- requirements.txt [The tools the API needs to function]
- helpers.py [Queries for the database 'SELECT']

## [0.2.5] - 2020-10-10

### Added
- Blueprints/states.py [Routes for the Table 'estados']
- Blueprints/messages.py [Routes for the Table 'messages']

### Changed
- models.py [Models of the State Object, Model of the Message Object]
- schemas.py [Schema from the State Model, Schema from the Message Model]
- requirements.txt [Deleted unused libraries]
- helpers.py [Queries for the database 'INSERT' and Field Verification]

## [0.2.6] - 2020-10-10

## Fixed
- AWS Lambda no longer shows error "name '_mysql' is not defined" [Appending mysql + pymysql at the start SQLALCHEMY_DATABASE_URI variable in config.py fixed it]

## Changed
- requirements.txt [Added mysql, mysql-client and wheel to the file as dependency]
- Changed s3 bucket [Changed value of property "s3_bucket":"lambda-python-eduardo" of zappa_settings.json]