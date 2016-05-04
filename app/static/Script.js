$(function() {
	$('.trigger').hide();
	$('#trigger').on('click', function() {
		$('.modal-trigger').leanModal()
	});
	// $('.modal-trigger').openModal();
});