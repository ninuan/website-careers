import os
from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = os.environ['DB_CONNECTION']
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem",
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    # print(result.all())
    jobs = []
    for row in result.all():
      # print(row._mapping)
      jobs.append(row._mapping)
  
    return jobs
  