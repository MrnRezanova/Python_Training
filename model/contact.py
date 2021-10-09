class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, address_1=None, home_phone=None,mobile_phone=None, work_phone=None, fax=None, email=None,
                 email_2=None, email_3=None, homepage=None, b_day=None, b_month=None, b_year=None, ann_day=None,
                 ann_month=None, ann_year=None, phone2=None, notes=None, id=None, all_phones_from_homepage=None,
                 all_email_from_homepage=None, all_email_from_db=None, all_phones_from_db=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.address_1 = address_1
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.ann_day = ann_day
        self.ann_month = ann_month
        self.ann_year = ann_year
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_email_from_homepage = all_email_from_homepage
        self.all_phones_from_db = all_phones_from_db
        self.all_email_from_db = all_email_from_db

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.address is None or other.address is None or self.address == other.address) \
               and (self.all_phones_from_homepage is None or other.all_phones_from_homepage
                    is None or self.all_phones_from_homepage == other.all_phones_from_homepage) \
               and (self.all_email_from_homepage is None or other.all_email_from_homepage
                    is None or self.all_email_from_homepage == other.all_email_from_homepage)