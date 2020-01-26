<!DOCTYPE html>
<html>

<head>
    <title>Consumer 2</title>
</head>

<body>
    <h1>Consumer 2</h1>
    <p>Show a list of all customers with name and an aggregated balance (sum of all product balances).</p>

    <table>
        <tr>
            <th>Name</th>
            <th>Balance sum</th>
        </tr>
        % for customerName, balanceSum in customers.items():
            <tr>
                <th>{{customerName}}</th>
                <th>{{balanceSum}}</th>
            </tr>
        % end
    </table>
</body>

</html>