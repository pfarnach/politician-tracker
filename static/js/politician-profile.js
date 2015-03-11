$(document).ready(function(){

	// politician profile image fade in when loaded inside politician_profile.html
	$('#politician-profile #profile-pic').hide();
	$('#politician-profile #profile-pic').fadeIn(800);

	$('#pol-subscribe .btn-subscribe').on('click', function(){

		var thisbtn = $(this);
		var pol_id = thisbtn.attr("data-pol-id");

		$.get('/profiles/subscribe_to_pol/', {pol_id: pol_id}, function() {
			thisbtn.children('span').html(' Watching');
			thisbtn.toggleClass('btn-primary btn-danger');
			thisbtn.toggleClass('btn-subscribe btn-unsubscribe');
		});
	});

	$('#pol-subscribe .btn-unsubscribe').on('click', function(){

		var thisbtn = $(this);
		var pol_id = thisbtn.attr("data-pol-id");

		$.get('/profiles/subscribe_to_pol/', {pol_id: pol_id}, function() {
			thisbtn.children('span').html(' Watch');
			thisbtn.toggleClass('btn-primary btn-danger');
			thisbtn.toggleClass('btn-subscribe btn-unsubscribe');
		});
	});

});