$(document).ready(function(){

	// -----------------------
	// Profile pic fade-in
	// -----------------------

	// politician profile image fade in when loaded inside politician_profile.html
	$('#politician-profile #profile-pic').hide();
	$('#politician-profile #profile-pic').fadeIn(1000);


	// -----------------------
	// Subscribe button
	// -----------------------

	// check to see if already subscribed
	var subscribe_btn = $('#subscribe-btn'),
		can_subscribe = subscribe_btn.attr("data-can-subscribe") === "true" ? true : false;

	// fade button in
	subscribe_btn.hide();
	subscribe_btn.fadeIn(1000);

	// change btn appearance if already subscribed
	if (!can_subscribe) {
		subscribe_btn.toggleClass('btn-subscribe btn-unsubscribe');
		subscribe_btn.toggleClass('btn-primary btn-danger');
		subscribe_btn.children('span').html(' Watching');
	}

	// let server determine if unsubscribe or subscribe call then change btn accordingly
	$('#subscribe-btn').on('click', function(){
		var pol_id = subscribe_btn.attr("data-pol-id");

		// subscribe ajax call
		$.get('/profiles/subscribe_to_pol/', {pol_id: pol_id}, function(data) {
			console.log(data);
			if (data === "subscribed") {
				subscribe_btn.children('span').html(' Watching');
				subscribe_btn.toggleClass('btn-primary btn-danger');
				can_subscribe = false;
			} else if (data === "unsubscribed") {
				subscribe_btn.children('span').html(' Watch');
				subscribe_btn.toggleClass('btn-primary btn-danger');
				can_subscribe = true;
			}
		});
	});
});