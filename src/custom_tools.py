from pydantic import BaseModel, Field
from langchain.tools import Tool

# CustomToolFunction class to create tools for various actions such as retrieving, updating account info
class CustomToolFunction():
    # Helper function to dynamically create tools
    def _create_tool(self, func, schema, name, description):
        return Tool(
            func=func,
            args_schema=schema,
            name=name,
            description=description
        )

    # The following functions can be implemented through  different methods, including diverse APIs designed for different purposes.
    def _get_account_info_(self, input):
        email = "example@gmail.com"
        name = "Alex"
        account_num = "347826483"
        return f"The input user ID is associated with the following information: \nEmail: {email} \nName: {name}\nAccount Number: {account_num}"

    def _update_account_info(self, attributes):
        return "Success"

    def _identity_verification(self, args):
        return "Approve"

    def _ordering(self, args):
        return "Success"

    def create_tool(self):
        class Getschema(BaseModel):
            user_id: str = Field(description="This variable stores user ID.")

        class Updateschema(BaseModel):
            attribute: str = Field(description="This variable stores a complete sentence that contains the attribute to update and the text for update.")

        # Tools created with the helper function and return the list of tools
        return [
            self._create_tool(self._get_account_info_, Getschema, 'Account_Information_Retriever', """
                This tool is connected to the backend of XYZ's company server where it is capable of retrieving the user's account information by user ID.
            """),
            self._create_tool(self._update_account_info, Updateschema, 'Account_Information_Updater', """
                This tool is connected to the backend of XYZ's company server where it is capable of updating the user's account information.
            """),
            self._create_tool(self._identity_verification, Getschema, 'Identity_Verification', """
                This tool is connected to the backend of XYZ's company server where it is capable of verifying the user's identity with user ID.
            """),
            self._create_tool(self._ordering, Getschema, 'Ordering', """
                This tool is connected to the backend of XYZ's company server where it is capable of ordering physical checks.
            """)
        ]