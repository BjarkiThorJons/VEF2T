<!DOCTYPE html>
<html>
<head>
	<title>Bílar</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<h1>Breyta bíl</h1>
	%for x in post:
		<p>{{x}} : {{post[x]}}</p>
	%end
	<form action="/bill" method="post">
	</form>
	<form action="/d" method="post">
		<h2>Breyta</h2>
		<input type="radio" name="bill" value="skarningarnumer">skarningarnumer<br>
		<input type="radio" name="bill" value="tegund">tegund<br>
		<input type="radio" name="bill" value="verksmidjunumer">verksmidjunumer<br>
		<input type="radio" name="bill" value="co2">co2<br>
		<input type="radio" name="bill" value="þyngd">þyngd<br>
		<input type="radio" name="bill" value="skodun">skodun<br>
		<input type="radio" name="bill" value="stada">stada<br>
		<input type="text" name="texti">
		<input type="submit" name="submit" value="Breyta"><br>
		<input type="submit" name="submit" value="delete">
	</form>
</body>
</html>