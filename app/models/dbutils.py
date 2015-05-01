from .. import db
import regs

def add_new_regid(reg_id, status):
	new_user = regs.User(reg_id, status)
	db.session.add(new_user)
	db.session.commit()    
	# TODO: return inserted primary key
	return 1   
