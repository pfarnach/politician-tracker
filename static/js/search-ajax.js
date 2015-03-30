$(document).ready(function(){
	
	// on load, create an empty list
	var politician_list = [], list_loaded=false;
	
	if (politician_list.length === 0) {
		$.get('/profiles/search_list/', function(data) {
			unpack_politician_list(data);
		});
	}

	// Unpacks JSON list from server and makes array of objects containing politician's data
	function unpack_politician_list(list) {
		search_list = [];
		for (var i=0; i < list.length; i++) {

			var name = list[i]['fields']['official_full_name'],
				chamber = list[i]['fields']['chamber'],
				state = list[i]['fields']['state'],
				district = typeof(list[i]['fields']['rep_district']) === "object" ? "" : "-"+list[i]['fields']['rep_district'],
				party = list[i]['fields']['party'],
				slug = list[i]['fields']['slug'];

			var pol = { name: name,
						chamber: chamber,
						state: state,
						district: district,
						party: party,
						slug: slug };

			search_list.push(pol);

		}
		generate_pol_html(search_list);
	}

	function generate_pol_html(list) {
		for (var i=0; i < list.length; i++) {
			// makes a url with the slug and puts it into li
			var url = '/profiles/' + list[i]['slug'];
			$('#search_results').append('<li><a href="'+ url +'">' + list[i]['name'] + '<span> ('+list[i]['state'] +list[i]['district']+ ")</span></a></li>");
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


