<!DOCTYPE html>
<html>

<head>
    <title>Consumer1</title>
</head>

<body>
    <h1>Consumer 1</h1>
    <p>Show a list of all customers with name, email and status</p>

    <table>
        <tr>
            <th>Name</th>
            <th>E-Mail</th>
            <th>Status</th>
        </tr>
        % for customer in customers:
            <tr>
                <td>{{customer['name']}}</td>
                <td>{{customer['email']}}</td>
                <td>{{customer['status']}}</td>
            </tr>
        % end
    </table>
</body>

</html>