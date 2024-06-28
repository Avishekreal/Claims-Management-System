<<<<<<< HEAD
import os
import unittest
from cms import ClaimsManagementSystem
from entities import Policyholder, Policy, Claim

class TestDatabaseIntegration(unittest.TestCase):
    db_name = 'test_cms.db'

      
        
        self.cms.create_policy(policy)
        retrieved_policy = self.cms.read_policy(1)
        self.assertEqual(retrieved_policy.policy_type, "Health")

    
        policy.policy_type = "Life"
        self.cms.update_policy(policy)
        retrieved_policy = self.cms.read_policy(2)
        self.assertEqual(retrieved_policy.policy_type, "Life")

    def test_delete_policy(self):
        policyholder = Policyholder(
            policyholder_id=6,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=3,
            policyholder_id=6,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        self.cms.delete_policy(3)
        retrieved_policy = self.cms.read_policy(3)
        self.assertIsNone(retrieved_policy)

    def test_create_and_read_claim(self):
        policyholder = Policyholder(
            policyholder_id=7,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=4,
            policyholder_id=7,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=1,
            policy_id=4,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        retrieved_claim = self.cms.read_claim(1)
        self.assertEqual(retrieved_claim.claim_amount, 500.0)

    def test_update_claim(self):
        policyholder = Policyholder(
            policyholder_id=8,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=5,
            policyholder_id=8,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=2,
            policy_id=5,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        claim.claim_status = "Approved"
        self.cms.update_claim(claim)
        retrieved_claim = self.cms.read_claim(2)
        self.assertEqual(retrieved_claim.claim_status, "Approved")

    def test_delete_claim(self):
        policyholder = Policyholder(
            policyholder_id=9,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=6,
            policyholder_id=9,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=3,
            policy_id=6,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        self.cms.delete_claim(3)
        retrieved_claim = self.cms.read_claim(3)
        self.assertIsNone(retrieved_claim)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
=======
# test_claims_management_system.py

import unittest
from cms import ClaimsManagementSystem
from entities import Policyholder, Policy, Claim

class TestDatabaseIntegration(unittest.TestCase):
    def setUp(self):
        db_name = "cms_db"
        user = "postgres"
        password = "password"
        host = "localhost"
        port = "5432"
        
        self.cms = ClaimsManagementSystem(db_name, user, password, host, port)

    def tearDown(self):
        with self.cms.db.connection.cursor() as cursor:
            cursor.execute("DELETE FROM claims")
            cursor.execute("DELETE FROM policies")
            cursor.execute("DELETE FROM policyholders")
            self.cms.db.connection.commit()

    def test_create_and_read_policyholder(self):
        policyholder = Policyholder(
            policyholder_id=None,  # SERIAL will auto-generate ID
            name="Avishek Gope",
            address="Raj pearl pg Noida sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishek06500@gmail.com"}
        )
        self.cms.create_policyholder(policyholder)
        retrieved_policyholder = self.cms.read_policyholder(policyholder.policyholder_id)
        self.assertEqual(retrieved_policyholder.name, "Avishek Gope")

    def test_create_and_read_policy(self):
        policyholder = Policyholder(
            policyholder_id=None,
            name="Jane Doe",
            address="456 Elm St, Springfield",
            contact_details={"phone": "555-5678", "email": "janedoe@example.com"}
        )
        self.cms.create_policyholder(policyholder)

        policy = Policy(
            policy_id=None,
            policyholder_id=policyholder.policyholder_id,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2024-12-31",
            premium_amount=1200.50,
            coverage_details={"coverage": "Full"}
        )
        self.cms.create_policy(policy)
        retrieved_policy = self.cms.read_policy(policy.policy_id)
        self.assertEqual(retrieved_policy.policy_type, "Health")

    def test_create_and_read_claim(self):
        policyholder = Policyholder(
            policyholder_id=None,
            name="Jim Beam",
            address="789 Maple St, Springfield",
            contact_details={"phone": "555-8765", "email": "jimbeam@example.com"}
        )
        self.cms.create_policyholder(policyholder)

        policy = Policy(
            policy_id=None,
            policyholder_id=policyholder.policyholder_id,
            policy_type="Car",
            start_date="2024-01-01",
            end_date="2024-12-31",
            premium_amount=800.75,
            coverage_details={"coverage": "Full"}
        )
        self.cms.create_policy(policy)

        claim = Claim(
            claim_id=None,
            policy_id=policy.policy_id,
            claim_date="2024-06-01",
            claim_amount=5000.00,
            claim_status="Pending",
            description="Car accident on highway",
            documents=["report.pdf", "photo.jpg"]
        )
        self.cms.create_claim(claim)
        retrieved_claim = self.cms.read_claim(claim.claim_id)
        self.assertEqual(retrieved_claim.claim_status, "Pending")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
>>>>>>> 328ceff (Add initial directory structure and files for CMS project)
