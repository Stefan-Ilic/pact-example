<!DOCTYPE html>
<html>

<head>
    <title>Consumer 3</title>
</head>

<body>
    <h1>Consumer 3</h1>
    <p>Allow to search for customers and show the details of all financial products.</p>

    <form>
        Customer ID: (use 1, 2, 3):<br>
        <input type="text" name="customerID" value="1">
        <br>
        <input type="submit" value="Submit">
    </form>

    <p>Showing details for customer {{customerName}}</p>
    <table>
        <tr>
            <th>Name</th>
            <th>Balance</th>
            <th>Product Code</th>
            <th>Interest Rate</th>
        </tr>
        % for product in products:
            <tr>
                <td>{{product['name']}}</td>
                <td>{{product['balance']}}</td>
                <td>{{product['productCode']}}</td>
                <td>{{product['interestRate']}}</td>
            </tr>
        % end
    </table>

</body>

</html>