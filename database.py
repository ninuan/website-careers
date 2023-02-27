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
    jobs = [row._asdict() for row in result.all()]
    # for row in result.all():
    #   # print(row._mapping)
    #   jobs.append(row._mapping)
  
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = " + id))
    rows = result.all()
    # print(rows[0])
    if len(rows) == 0:
      return None
    else:
      row_dict = [rows[0]._asdict()]
      # print(row_dict)
      return row_dict