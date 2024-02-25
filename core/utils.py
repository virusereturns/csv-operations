from faker import Faker


def generate_people_list(amount):
    fake = Faker()
    people = []
    for _ in range(amount):
        people.append([
            fake.name(), fake.random_int(min=18, max=100, step=1), fake.email(), fake.phone_number()
        ])
    return people


def generate_person():
    fake = Faker()
    return {
        'name': fake.name(),
        'age': fake.random_int(min=18, max=100, step=1),
        'email': fake.email(),
        'phone': fake.phone_number(),
    }


def people_generator(amount):
    fake = Faker()
    for _ in range(amount):
        yield {
            'name': fake.name(),
            'age': fake.random_int(min=18, max=100, step=1),
            'email': fake.email(),
            'phone': fake.phone_number(),
        }
