<!DOCTYPE html>
<html>
<head>
	<title>Tónleikar</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<h1>Tónleikar</h1>
	%for post in posts["results"]:
		<h2>Nafn tónleika</h2>
		<p>{{post["eventDateName"]}}</p>
		<h2>Tegund tónleika</h2>
		<p>{{post["name"]}}</p>	
		<h2>Dagsetning</h2>
		<p>{{post["dateOfShow"]}}</p>
		<h2>Umsjón</h2>	
		<p>{{post["userGroupName"]}}</p>
		<h2>Staðsettning</h2>	
		<p>{{post["eventHallName"]}}</p>	
		<img src='{{post["imageSource"]}}'>
</body>
</html>