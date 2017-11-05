<!DOCTYPE html>
<html>
<head>
	<title>Bílar</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<h1>Leita af bíl</h1>
	<form action="/bill" method="post">
		<input type="text" name="bill">
		<input type="submit" name="leita" value="leita">
	</form>
	<h1>Bæta við Bíl</h1>
	<form action="/+" method="post">
		skraningarnumer:<br>
		<input type="text" name="skraningarnumer"><br>
		tegund<br>
		<input type="text" name="tegund"><br>
		verksmidjunumer<br>
		<input type="text" name="verksmidjunumer"><br>
		skraningadagur<br>
		<input type="text" name="skraningadagur"><br>
		co2<br>
		<input type="text" name="co2"><br>
		þyngd<br>
		<input type="text" name="t"><br>
		skodun<br>
		<input type="text" name="skodun"><br>
		stada<br>
		<input type="text" name="stada"><br>
		<input type="submit" name="submit" value="Bæta við">
	</form>
</body>
</html>