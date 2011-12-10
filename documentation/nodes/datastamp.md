---
layout: reference
title: Data Stamp Node
image: csv
---
Copy input geometry for each row in a [CSV file](http://en.wikipedia.org/wiki/Comma-separated_values). The first row is skipped by default since we assume it is the header row. It copies the incoming shape geometry and provides a number of stamp variables that you can refer to. If you provide a template shape it will be used as a point source and for each row, the source shape will be translated to the point.

The data stamp node is quite powerful. Read the [page on data stamping](../using/data-stamping.html) for an introduction.

CSV files can be exported from spreadsheet programs such as Microsoft Excel, Apple Numbers or Google Docs or from data mining applications such as [Pattern](http://www.cpl.ua.ac.be/pages/pattern).

Parameters
----------
* **File**: The CSV file.
* **Table Name**: The prefix for stamping. Normally you only change this when using multiple data stamp nodes.

Stamp Variables
---------------
The following data stamp variables are available (with the default "data" table name):

* **data_row_count**: The amount of rows in the file
* **data_column_count**: The amount of columns in the file
* **data_row_index**: The current index of the row, starting from zero.
* **data_row_position**: The relative position in the file, from 0.0-1.0
* **data_value_0**: The value of the first column. If the value can be parsed as a number, it will.
* **data_value_1**: The value for the second column.
* **data_relative_value_0**: The total of the column divided by the current value. A value between 0.0 and 1.0. Only available if the column has numbers in it.
* **column_total_0**: The total value for this column. Only available if the column has numbers in it.
