$('#id_servicos').change(function(e) {

	var id_do_estado = $('#id_servicos').val();
	$.ajax({
		url: '127.0.0.1:8000/precos/',
		type:'GET',
		data: {id: id_do_estado},
	})
	.done(function(precos) {
		return precos['id_servicos']
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
});