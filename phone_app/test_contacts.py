import unittest


class PhoneBookTest(unittest.TestCase):

	def setup(self):
		phonebook = Phonebook()
		self.contactList = []
		self.contacts_count = len(contactList)
		self.contacts_count = 50
		self.all_contacts = {}
		

	def test_add_contact(self):
		new_contact = contact.add_contact("Mary", 07245698500)
		current_contactList = contactList.append(new_contact)
		self.assertEqual(len(current_contactList) - self.contacts_count, 1)



	def test_update_contact(self):
		contact = Contact("Mary",076398742)
		updated_contact = contact.update_contact("Mary", 0789654123)
		self.assertNotEqual(contact, updated_contact, msg= "no change made")

	
		
	def test_delete_contact(self):
		contact3 = Contact("Ary", 07230754545)
		contact3.delete_contact()
		self.assertEqual(len(contactList), 49)
		

	def test_view_contact(self):
		contact4 = Contact("Lillian", 078903455)
		contact4.test_view_contact(Lillian)
		self.assertEqual({"Lillian": 78903455}, msg="contact not found")
		

	def test_duplicate_contacts(self):
		contact5 = contact5("Olive",072569983)
		contact6 = contact5("Olive", 072569983)
		error = "contact already exists"
		self.assertEqual(error, contact6)

		
		


if __name__ == '__main__':
	unittest.main()
