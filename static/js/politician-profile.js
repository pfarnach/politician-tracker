var pol_id;

$(document).ready(function(){

	pol_id = $('#politician-name').attr("data-pol-id");

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
		subscribe_btn.children('i').toggleClass('glyphicon-eye-open glyphicon-eye-close');
		subscribe_btn.children('span').html(' Unwatch');
	}

	// let server determine if unsubscribe or subscribe call then change btn accordingly
	$('#subscribe-btn').on('click', function(){

		// disable button until AJAX request goes through
		$(this).prop("disabled",true);

		// subscribe AJAX call
		$.get('/profiles/subscribe_to_pol/', {pol_id: pol_id}, function(data) {

			// enable button after AJAX request goes through
			$('#subscribe-btn').prop("disabled",false);

			if (data === "subscribed") {
				subscribe_btn.children('span').html(' Unwatch');
				subscribe_btn.toggleClass('btn-primary btn-danger');
				subscribe_btn.children('i').toggleClass('glyphicon-eye-open glyphicon-eye-close');
				can_subscribe = false;
			} else if (data === "unsubscribed") {
				subscribe_btn.children('span').html(' Watch');
				subscribe_btn.toggleClass('btn-primary btn-danger');
				subscribe_btn.children('i').toggleClass('glyphicon-eye-open glyphicon-eye-close');
				can_subscribe = true;
			}
		});
	});

	// unsubscribe button on view_subscriptions page
	$('.subscribe-btn-subscriptions').on('click', function(){
		var this_button = $(this);
		var pol_id_subscriptions = this_button.attr('data-pol-id-subscriptions');
		// disable button until AJAX request goes through
		this_button.prop("disabled",true);

		// subscribe AJAX call
		$.get('/profiles/subscribe_to_pol/', {pol_id: pol_id_subscriptions}, function(data) {
			
			// enable button after AJAX request goes through
			this_button.prop("disabled",false);
			this_button.toggleClass('btn-primary btn-danger');
			this_button.children('i').toggleClass('glyphicon-eye-open glyphicon-eye-close');
		});
	});

});


// -----------------------
// Angular.js widgets
// -----------------------

angular.module('PoliticianProfile', ['ngTagsInput'])

	.config(function($interpolateProvider, $httpProvider) {
		$interpolateProvider.startSymbol('{[{');
		$interpolateProvider.endSymbol('}]}');
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	})

	.directive('moneyInfo', function () {
		return {
			restrict: 'E',
			templateUrl: '/static/moneyinfo.html'
		};
	})

	.directive('tooltip', function() {
		return {
			restrict: 'A',
			link: $('[data-toggle="tooltip"]').tooltip({ placement : 'top' })
		};
	})

	.controller('MoneyController', function($scope, $http) {
		$scope.fade = false;

		// do AJAX request to server to get money info
		// fetch and display photos
		var fetchMoneyInfo = function(pol_id) {
			$http.get('/profiles/get_money_info/', {params: {pol_id: pol_id}})
				.success(function(data, status, headers, config) {

					$scope.net_low = data[0]['fields']['net_low'];
					$scope.net_high = data[0]['fields']['net_high'];
					$scope.top_contributors = JSON.parse(data[0]['fields']['top_contributor']);
					$scope.top_industries = JSON.parse(data[0]['fields']['top_industry']);

					// convert string integer values to integers
					$scope.top_contributors.forEach(function(d) {
						d['indivs'] = +d['indivs'];
						d['total'] = +d['total'];
						d['pacs'] = +d['pacs'];
					});

					$scope.top_industries.forEach(function(d) {
						d['indivs'] = +d['indivs'];
						d['total'] = +d['total'];
						d['pacs'] = +d['pacs'];
					});

					$scope.fade = true;

				})
				.error(function(data, status, headers, config) {
					console.log('AJAX request error');
				});
			};

		fetchMoneyInfo(pol_id);

			// for order preference
		$scope.orderPrefOrg = "-total";
		$scope.orderPrefIndustry = "-total";
		$scope.selectedHeaderOrg = "total";
		$scope.selectedHeaderIndustry = "total";
		$scope.ascendingOrg = true;
		$scope.ascendingIndustry = true;

		// orders how entry rows are displayed (toggles between asc and desc order)
		$scope.selectOrderOrg = function(pref) {

			$scope.selectedHeaderOrg = pref;
			if (pref == $scope.orderPrefOrg) {
				$scope.orderPrefOrg = "-" + pref;
				$scope.ascendingOrg = false;
			} else {
				$scope.orderPrefOrg = pref;
				$scope.ascendingOrg = true;
			}
		};

		// for Industry table
		$scope.selectOrderIndustry = function(pref) {

			$scope.selectedHeaderIndustry = pref;
			if (pref == $scope.orderPrefIndustry) {
				$scope.orderPrefIndustry = "-" + pref;
				$scope.ascendingIndustry = false;
			} else {
				$scope.orderPrefIndustry = pref;
				$scope.ascendingIndustry = true;
			}
		};
	})

	.directive('articleDisplay', function () {
		return {
			restrict: 'E',
			templateUrl: '/static/articledisplay.html'
		};
	})

	.controller('ArticleController', function($scope, $http) {

		$scope.addArticleEnabled = false;
		$scope.addedSuccess = false;
		$scope.articles_present = false;
		$scope.articles = []

		var fetchArticles = function() {
			$http.get('/profiles/get_articles/', {params: {pol_id: pol_id}})
				.success(function(data, status, headers, config) {
					console.log(data);

					if (data['articles_present']) {
						$scope.articles_present = true;
						// send data to function to get put cleaned up and put into scope
						generate_article_list(data['articles']);
					} else {
						$scope.articles_present = false;
					}
					// console.log(JSON.parse(data['articles'][0]['tags']));
					$scope.is_authenticated = data['is_authenticated'];
				})
				.error(function(data, status, headers, config) {
					console.log('AJAX request error');
				});
		};

		fetchArticles();

		var generate_article_list = function(articles) {
			$scope.articles = []
			for (var i = 0; i < articles.length; i++) {
				articles[i]['tags'] = JSON.parse(articles[i]['tags']);
				$scope.articles.push(articles[i]);
			}
			console.log($scope.articles);
		};

		$scope.enableAddArticle = function() {
			$scope.addArticleEnabled = true;
		};

		$scope.disableAddArticle = function() {
			$scope.resetAddArticle();
		};

		$scope.resetAddArticle = function() {
			$scope.addArticleEnabled = false;
			$scope.article.url = "";
			$scope.article.title = "";
			$scope.article.tags = [];
			$scope.articleForm.$setPristine();
		};

		// form validation source: http://codepen.io/sevilayha/pen/xFcdI?editors=101
		$scope.addArticle = function() {
			if ($scope.articleForm.$valid) {
				console.log($scope.article);

				var article_data = angular.copy($scope.article);
				article_data['pol'] = pol_id;
				$scope.resetAddArticle();

				$http.post('/profiles/post_article/', article_data)
					.success(function(data) {
						console.log(data);
						$scope.addedSuccess = true;
					})
					.error(function(data){
						console.log('Error posting article info');
					});
			}
		};
	});
