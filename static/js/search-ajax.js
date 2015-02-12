$(document).ready(function(){
	
	// on load, create an empty list
	var politician_list = [], list_loaded=false;
	
	$(".sidebar-nav").on('mouseenter', function(){
		
		// if list is empty, go fetch it from server
		if (!list_loaded) {
			if (politician_list.length === 0) {
				$.get('/profiles/search_list/', function(data) {
					politician_list = data;
					unpack_politician_list(politician_list);
				});
			}	
		}
		list_loaded=true;
		console.log('list loaded');
	});
	

	// Unpacks JSON list from server and makes array of objects containing politician's data
	function unpack_politician_list(list) {
		search_list = [];
		for (var i=0; i < list.length; i++) {
			var pol_name = politician_list[i]['fields']['name'];
			var pol_chamber = politician_list[i]['fields']['chamber'];
			var pol_district = politician_list[i]['fields']['district'];
			var pol_party = politician_list[i]['fields']['party'];
			var pol_slug = politician_list[i]['fields']['slug'];
			var pol = {name: pol_name, chamber: pol_chamber, district: pol_district, party: pol_party, slug: pol_slug};
			search_list.push(pol);

		}
		generate_pol_html(search_list);
	}

	function generate_pol_html(list) {
		for (var i=0; i < list.length; i++) {
			// makes a url with the slug and puts it into li
			var url = '/profiles/' + list[i]['slug'];
			$('#search_results').append('<li><a href="'+ url +'">' + list[i]['name'] + "</a></li>");
		}
		// $('#search_results li').css({"margin": "0", "padding": "0"});  not affecting it but it does work
		$('#search_results').children().hide();
	}

	// regex expression to see if user inpt (filter) is contained in list names
	$( "#sidebar_search" ).keyup(function() {

		filter = $(this).val();

		// checks to make sure at least x amount of characters have been typed in first
		if (filter.length >= 4) {
			$("#search_results li").each(function() {
				console.log($(this).text());
				if ($(this).text().search(new RegExp(filter, "i")) < 0) {
					$(this).hide();
				// Show the list item if the phrase matches and increase the count by 1
				} else {
					$(this).show();
				}
			});
		} else {
			$("#search_results li").hide();
		}
	});
});


