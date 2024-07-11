================================
CLI Tools for Amdocs ConnectX
================================

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/connectX.png
   :alt: ConnectX Logo

.. contents:: Table of Contents
   :local:

Introduction
============

The ctxcli package provides Command Line Interface (CLI) tools for Amdocs ConnectX. These tools allow authorized ConnectX users to perform various operations on the system.

Installation
============

Before installing ctxcli, ensure that `Python <https://www.python.org/downloads/>`__ and `pip <https://pip.pypa.io/en/stable/installing/>`__ are installed on your system.

To install ctxcli from PyPI, execute the following command::

    pip install ctxcli

Authentication
==============

Before running any command, you need to authenticate by running the 'auth' command. Use the following command to authenticate::

    ctxcli auth

You will be prompted to enter your tenant, environment (dev, ppe, prod), username, and password.

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/auth-screenshot.png
   :alt: Auth Screenshot
   
You can check the validity of your current session in any time by using the authcheck command. This command verifies whether you are authenticated and provides information about your active session::

    ctxcli authcheck

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/authcheck-screenshot.png
   :alt: Auth Check Screenshot

Commands
========

The ctxcli commands are divided into the following categories: Users, Tenant, and Migration.

Users
-----

To list all the users in the system, execute the following command::

    ctxcli user list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/users-list-screenshot.png
   :alt: Users Screenshot

Tenant
------

To list all the sub-tenants in the system, execute the following command::

    ctxcli tenant list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/tenants-list-screenshot.png
   :alt: Tenants Screenshot

Migration
---------

To list all the migration files in the system, execute the following command::

    ctxcli migration file list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/migration-files-screenshot.png
   :alt: Migration Files Screenshot



Business Units
--------------

List all business units
~~~~~~~~~~~~~~~~~~~~~~~

To list all the business units in the system, execute the following command::

    ctxcli business-unit list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/business-units-screenshot.png
   :alt: Migration Files Screenshot

Assign Users to Business Units in Bulk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To add users to business units, execute the following command::

	ctxcli business-unit add-users --file <file_path>
	
This command requires a CSV file that contains the necessary user information. You can specify the path
to this CSV file using the --file argument followed by the path to your file.
The following headers are required in the first row of the CSV file:


.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - Field
     - Details
   * - ``business_unit_id``
     - The internal ID of the Business Unit the user should be assigned to.

   * - ``username``
     - The username of the user that should be assigned to the Business Unit.

    
The command will read each line of the CSV file and attempt to add the specified user to the corresponding Business Unit.

You can download the CSV template `here <https://assets.ppe.amdocs-dbs.cloud/ctxcli/bu_users.csv>`__.

Create Business Units in Bulk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create multiple business units, execute the following command::

	ctxcli business-unit create --file <file_path>
	
This command requires a CSV file that contains the necessary user information. You can specify the path
to this CSV file using the --file argument followed by the path to your file.
The following headers are required in the first row of the CSV file:


.. list-table::
   :widths: 45 50
   :header-rows: 1

   * - Field
     - Details
   * - ``name``
     - The name of the Business Unit.

   * - ``description``
     - The name of the Business Unit.
    
   * - ``businessunitspec.butype``
     - The description of the Business Unit Specification.

   * - ``businessunitspec.buhref``
     - The API endpoint URL of the Business Unit Specification.
     
   * - ``speccharacteristics.names``
     - The names (in comma-separated format) of the characteristics according to the selected Business Unit Specification.
     
   * - ``speccharacteristics.values``
     - The values (in comma-separated format) of the characteristics corresponding to the names listed in the 'speccharacteristics.names' field. The order of the values should match the order of the names.
     
   * - ``externalid``
     - The external unique identifier for the Business Unit.

   * - ``address.street1``
     - The primary street address line for the Business Unit.
     
   * - ``address.street2``
     - The secondary street address line for the Business Unit.

   * - ``address.city``
     - The city where the Business Unit is located.
     
   * - ``address.postcode``
     - The postal code for the Business Unit's address.
     
   * - ``address.stateorprovince``
     - The state or province where the Business Unit is located.
     
   * - ``address.country``
     - The country where the Business Unit is located.
     
   * - ``phone``
     - The primary phone number for the Business Unit.
     
   * - ``childof.id``
     - The unique identifier of the parent Business Unit.
     
   * - ``childof.href``
     - The API endpoint URL for the parent Business Unit.

This list now only contains field names and their descriptions.

    
The command executes the POST /businessUnit API for every line in the CSV file, using the corresponding field values from the CSV. For mandatory fields, data format, and more information, please refer to `the official API documentation <https://knowledge.amdocs-dbs.com/reference/businessunitcontroller_create>`_.

You can download the CSV template `here <https://assets.ppe.amdocs-dbs.cloud/ctxcli/business_units.csv>`__.




Orders
------

To export orders to an Excel file for a specified date range execute the following command:

.. code:: bash

   ctxcli order export --start-date <start_date> --end-date <end_date> --output <file_path>

while:

.. list-table::
   :widths: 35 60
   :header-rows: 1

   * - Field
     - Details
   * - ``--start-date <start_date>``
     - The start date for the order export in the format `YYYY-MM-DD`.

   * - ``--end-date <end_date>``
     - The end date for the order export in the format `YYYY-MM-DD`.
     
   * - ``--output <file_path>``
     - The file path for the output Excel file. The file will be created if it does not exist.




Customers
--------------

Delete multiple individuals
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete multiple individuals execute the following command:

  ctxcli customer delete --file <file_path>

This command requires a CSV file that contains the necessary user information. You can specify the path
to this CSV file using the --file argument followed by the path to your file.
The following headers are required in the first row of the CSV file:


.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - Field
     - Details
   * - ``individual_id``
     - The internal ID of the individual.

   * - ``status``
     - The status of the customer. Status can be "Initialized", "Approved" or "Activated".

The command will read each line of the CSV file and attempt to delete all entities related to the specified individual.

Delete single individual
~~~~~~~~~~~~~~~~~~~~~~~~

To delete single individual execute the following command:

  ctxcli customer delete --individual-id <individual id>

The user will be prompted to select customer status. The user navigates the list using the arrow keys and selects a status by pressing Enter.
The command will attempt to delete all entities related to the specified individual.



License
=======

Copyright 2024 Amdocs