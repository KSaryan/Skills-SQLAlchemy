"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
#   1. This will return a query. You need to add .first() or .one() to 
# get an object. 


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
#   2. An association table is a table that links two tables together. There may
# be two tables, for example, a table of children and a table of toys. One child may 
# play with many toys at once, and a toy may be played with by several children at once. The 
# relationship between these two tables is many to many. But you can't really do that,
# so you create an association table, playtime, to manage that relationship. Playtime will 
# have a one to many relationship with the children and toys tables (each child can have one 
# playtime, and each toy one playtime, but playtime can have many children and toys).We don't
# actually want any information about the playtime besides who was playing with what.
# And playtime won't contain any information besides playtime_id, child_id and toy_id. We never will
# be querying playtime, just using the relationship it creates to allow us to run queries 
# about which (or how many) toys a kid is playing with and which (or how many) kids are 
# playing with a toy. If we kept information, like when the play happened or for how long,
# then playtime would by a middle table.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').one()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    # model_info = db.session.query(Model.name,
    #                           Brand.name,
    #                           Brand.headquarters).join(Brand).filter(Model.year==year).all()
    
    # print str(year) + " Models:"
    # for q in model_info:
    #     """I know that these are name tuples, so I wanted to use that to
    #     access the values in the tuples, but I couldn't figure out what the name
    #     was for the first item in the tuple, since there are two names. I don't know
    #     how to get this information"""
    #     print "Model: %s, Brand: %s, Headquarters: %s" %(q[0], q.name, q.headquarters)

    #OR

    model_info = db.session.query(Model).filter_by(year=year).all()
    print str(year) + " Models:"
    if model_info:
        for q in model_info:
            print "Model: %s, Brand: %s, Headquarters: %s" %(q.name, 
                                                             q.brands.name, 
                                                             q.brands.headquarters)
    else:
        print "None"



def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brand_info = db.session.query(Brand).all()

    for brand in brand_info:
        print 'Brand: ' + brand.name
        print 'Models:'
        for model in brand.models:
            print model.name, model.year 
        print '\n'


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    newstr = '%{}%'.format(mystr)
    brands = Brand.query.filter(Brand.name.like(newstr)).all()
  
    return brands


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    btwmodels= Model.query.filter(Model.year >= start_year, 
                                  Model.year < end_year).all()

    return btwmodels

