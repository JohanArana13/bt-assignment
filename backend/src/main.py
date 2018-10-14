from .entities.entity import Session, engine, Base
from .entities.url import Url

Base.metadata.create_all(engine)

session = Session()

urls = session.query(Url).all()

if len(urls) == 0:
    test_assignment = Url("example.com", "123ABC", "script")
    session.add(test_assignment)
    session.commit()
    session.close()

    urls = session.query(Url).all()

print('### Urls:')
for url in urls:
    print('({url.id}) {url.long_url} - {url.short_url}')