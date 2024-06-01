# seed.py

from app import db
def seed_data():
    from app.models.userRole import UserRole
    from app.models.permissions import Permission
    from app.models.rolePermissionMapping import RolePermissionMap
    from app.models.company import Company  # Import the Company model
    from app.models.customers import Customers  # Import the Customer model
    from app.models.moduleProfile import ModuleProfile  # Import the ModuleProfile model
    from app.models.basePlan import BasePlan  # Import the BasePlan model
    from app.models.companyPlan import CompanyPlan  # Import the CompanyPlan model
    from app.models.users import User  # Import the User model
    from app.models.enums.enums import IndustryEnum, DepartmentEnum, CustomerTypeEnum, UserStatusEnum

    try:
        # Begin a transaction
        with db.session.begin_nested():
            # Create a company with dummy values
            dummy_company = Company(
                company_name="Dummy Company",
                customer_name="John Doe",
                address="1234 Elm Street",
                phone="123-456-7890",
                website="http://dummycompany.com",
                state="CA",
                city="Los Angeles",
                zip_code="90001",
                customer_type=CustomerTypeEnum.OTHER,  # Replace with actual enum value
                industry=IndustryEnum.OTHER,  # Replace with actual enum value
                subIndustry=IndustryEnum.OTHER,  # Replace with actual enum value
                department=DepartmentEnum.OTHER,  # Replace with actual enum value
                subDepartment=DepartmentEnum.OTHER  # Replace with actual enum value
            )
            db.session.add(dummy_company)
            db.session.flush()  # Flush to get the company ID

            # Create the 'superuser' role linked to the company
            superuser_role = UserRole(
                title='superuser',
                description='Superuser role with all permissions',
                slug='superuser',
                company_id=dummy_company.id
            )
            db.session.add(superuser_role)
            db.session.flush()  # Flush to get the role ID

            # Create permissions
            permission1 = Permission(title='permission1', description='Permission 1', slug='permission1')
            permission2 = Permission(title='permission2', description='Permission 2', slug='permission2')
            permission3 = Permission(title='permission3', description='Permission 3', slug='permission3')
            permission4 = Permission(title='permission4', description='Permission 4', slug='permission4')
            permission5 = Permission(title='permission5', description='Permission 5', slug='permission5')

            db.session.add(permission1)
            db.session.add(permission2)
            db.session.add(permission3)
            db.session.add(permission4)
            db.session.add(permission5)
            db.session.flush()  # Flush to get the permission IDs

            # Map permissions to the 'superuser' role
            role_permission_map1 = RolePermissionMap(role_id=superuser_role.id, permission_id=permission1.id)
            role_permission_map2 = RolePermissionMap(role_id=superuser_role.id, permission_id=permission2.id)
            role_permission_map3 = RolePermissionMap(role_id=superuser_role.id, permission_id=permission3.id)
            role_permission_map4 = RolePermissionMap(role_id=superuser_role.id, permission_id=permission4.id)
            role_permission_map5 = RolePermissionMap(role_id=superuser_role.id, permission_id=permission5.id)

            db.session.add(role_permission_map1)
            db.session.add(role_permission_map2)
            db.session.add(role_permission_map3)
            db.session.add(role_permission_map4)
            db.session.add(role_permission_map5)
            db.session.flush()  # Flush to ensure all mappings are saved

            # Create a customer and link it to the dummy company
            dummy_customer = Customers(
                company_id=dummy_company.id,
                name="Jane Smith",
                email="jane.smith@example.com",
                address="5678 Oak Street",
                phone="987-654-3210",
                website="http://janesmith.com",
                state="CA",
                city="San Francisco",
                zipcode="94102",
                customer_type="Type A",
                subType="SubType A",
                status="Active",
                subStatus="Primary",
                leadSource="Online",
                leadStatus="Interested",
                pipelineStatus="New",
                pipelineSubStatus="Initial Contact",
                title="CEO",
                bpStatus="Primary",
                relationshipToCustomer="Direct",
                primaryAssignment="John Doe",
                secondaryAssignment={"support": "Jane Doe"},
                subscriptionStatus="Subscribed",
                customFieldDropDown="Option1",
                customFieldPrice=1000.0,
                customFieldDates=db.func.now(),
                nextFollowUpDate=db.func.now(),
                customFields={"field1": "value1"},
                notes={"note1": "This is a note"},
                fed_id="FED123",
                w9_form="W9-123",
                irs="IRS-123"
            )
            db.session.add(dummy_customer)
            db.session.flush()  # Flush to get the customer ID

            # Create a module profile with dummy values
            module_profile = ModuleProfile(
                profile_name="Basic Profile",
                kb=True,
                call=False,
                assistants=True,
                chat_with_documents=True
            )
            db.session.add(module_profile)
            db.session.flush()  # Flush to get the module profile ID

            # Create a base plan and map it with the module profile
            base_plan = BasePlan(
                plan_name="Basic Plan",
                plan_type="Standard",
                module_profile_id=module_profile.id,
                no_of_emails_per_day=100,
                no_of_emails_per_month=3000,
                no_of_minutes_per_day=60,
                no_of_calls_per_month=200,
                llms=["llm1", "llm2"],
                max_allowed_token=5000,
                max_number_of_kb=10,
                max_number_of_action=50,
                assistants_daily_budget={"assistant1": 100, "assistant2": 150},
                max_no_assistants=5,
                price=49.99,
                notes={"note1": "This is a note"}
            )
            db.session.add(base_plan)
            db.session.flush()  # Flush to get the base plan ID

            # Create a company plan for the dummy company
            company_plan = CompanyPlan(
                plan_type="Premium",
                llms=["llm1", "llm2"],
                is_active=True,
                visibility_profile="High",
                assistant_daily_budget=200.0,
                assistant_monthly_budget=5000.0,
                no_of_emails_per_month=10000,
                no_of_calls_per_month=500,
                no_of_emails_per_day=300,
                no_of_calls_per_day=50,
                max_allowed_token=10000,
                max_number_of_kb=20,
                max_number_of_action=100,
                max_no_assistants=10,
                plan_expiry_date=db.func.now(),
                assistants_daily_budget={"assistant1": 200, "assistant2": 300},
                company_id=dummy_company.id,
                base_plan_id=base_plan.id,
                notes={"note1": "This is a company plan note"}
            )
            db.session.add(company_plan)
            db.session.flush()  # Flush to get the company plan ID

            # Create a dummy user for the company with the superuser role
            dummy_user = User(
                name="Super User",
                email="superuser@example.com",
                password="password",  # In a real application, ensure this is hashed
                phone="123-456-7890",
                status=UserStatusEnum.ACTIVE,  # Replace with actual enum value
                user_role_id=superuser_role.id,
                company_id=dummy_company.id,
                department=DepartmentEnum.OTHER,  # Replace with actual enum value
                created_by="admin",
                updated_by="admin"
            )
            db.session.add(dummy_user)
            db.session.flush()  # Flush to get the user ID

        # Commit the transaction if no errors occurred
        db.session.commit()
        print("Database seeded with superuser role, permissions, dummy company, customer, module profile, base plan, company plan, and user!")
    except Exception as e:
        # Rollback the transaction if an error occurred
        db.session.rollback()
        print(f"An error occurred: {e}")

# Make sure to call the seed_data function in the script

if __name__ == "__main__":
    from app import create_app

    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_data()
