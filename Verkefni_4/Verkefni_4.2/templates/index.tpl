% include('templates/header.tpl')
<main>
	<a href="/">Upphafssíða</a>
	<h1>{{ title }}</h1>
	<img src="{{ photo }}">
	<p>
		{{ text }}
	</p>
</main>
% include('templates/footer.tpl')