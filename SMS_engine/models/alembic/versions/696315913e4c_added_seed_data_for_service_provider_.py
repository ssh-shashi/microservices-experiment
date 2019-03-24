"""added seed data for service_provider_config table

Revision ID: 696315913e4c
Revises: be0a9c7c723a
Create Date: 2017-02-23 19:17:41.709938

"""

# revision identifiers, used by Alembic.

from media_engine.models.provider import ServiceProviderConfig,ServiceProvider

revision = '696315913e4c'
down_revision = 'be0a9c7c723a'
branch_labels = None
depends_on = None

from alembic import op
from datetime import datetime



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    sql_sp = conn.execute("SELECT * FROM {}".format(ServiceProvider.__tablename__))
    results = sql_sp.fetchall()
    for row in results:
        sp_config_obj = conn.execute("SELECT id FROM {} WHERE api_url=('{}')".format(ServiceProviderConfig.__tablename__, row.api_url))
        res=sp_config_obj.fetchall()
        if res:
            update_stmt = "UPDATE {} set sp_config_id=('{}') WHERE id=('{}')".format(ServiceProvider.__tablename__, res[0][0],
                                                                                     row.id)
            conn.execute(update_stmt)
        else:
            conn.execute(
                "INSERT IGNORE INTO {} (name, address,contact,api_url,api_port,send_sms_function,dummy_status,module,route_tag,balance_check_url,route_type,mms_api_url,created_on) VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}');".format(
                    ServiceProviderConfig.__tablename__, row.name, row.address, row.contact, row.api_url, row.api_port,
                    row.send_sms_function, row.dummy_status, row.module, row.route_tag, row.balance_check_url,
                    row.route_type, row.mms_api_url,datetime.now()))
            sp_config_obj = conn.execute(
                "SELECT id FROM {} WHERE api_url=('{}')".format(ServiceProviderConfig.__tablename__, row.api_url))
            res = sp_config_obj.fetchall()
            update_stmt = "UPDATE {} SET sp_config_id=('{}') WHERE id=('{}')".format(ServiceProvider.__tablename__, res[0][0],
                                                                                     row.id)
            conn.execute(update_stmt)

            ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
