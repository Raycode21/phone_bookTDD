import unittest


class PhoneBookTest(unittest.TestCase):

	def setup(self):
		phonebook = Phonebook()
		self.contactList = []
		self.contacts_count = len(contactList)
		self.contacts_count = 50
		self.all_contacts = {}
		

	def test_add_contact(self):

		new_contact = contact.add_contact("Mary", 7245698500)
		current_contactList = contactList.append(new_contact)
		self.assertEqual(len(current_contactList) - self.contacts_count, 1)



		
	def test_update_contact(self):
		contact = Contact("Mary",256398742)
		updated_contact = contact.update_contact("Mary", 789654123)
		self.assertNotEqual(contact, updated_contact, msg= "no change made")


	def test_input_type(self):
		contact3 = contact.create_contact(0123, 777896589)



	
		
	def test_delete_contact(self):
		contact3 = Contact("Ary", 890754545)
		contact3.delete_contact()
		self.assertEqual(len(contactList), 49)
		

	def test_view_contact(self):
		contact4 = Contact("Lillian", 78903455)
		contact4.test_view_contact(Lillian)
		self.assertEqual({"Lillian": 78903455}, msg="not found")
		

	def test_duplicate_contacts(self):
		


if __name__ == '__main__':
	unittest.main()
