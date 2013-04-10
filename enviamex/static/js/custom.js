$(document).ready(function(){
	// Menu
    $("#menu li").hover(function(){
		$('ul:first',this).slideDown('700');
    }, function(){
		$('ul:first',this).stop().slideUp('700');
    });
	// Clear search form
    $.fn.autoClear = function () {
        $(this).each(function() {
            $(this).data("autoclear", $(this).attr("value"));
        });
        $(this)
            .bind('focus', function() {  
                if ($(this).attr("value") == $(this).data("autoclear")) {
                    $(this).attr("value", "");
                }
            })
            .bind('blur', function() {  
                if ($(this).attr("value") == "") {
                    $(this).attr("value", $(this).data("autoclear"));
                }
            });
        return $(this);
    }
    $('.search-text-box,.rss-text-box').autoClear();
	
	// Buttom up
	$(".up").hide();
	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				$('.up').fadeIn();
			} else {
				$('.up').fadeOut();
			}
		});
		$('.up').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});   
	});	

	// Social icons
	$(".social-icons a").hover(function(){
		$(this).stop().animate({'top': '0'}, 300 );
	}, function(){
		$(this).stop().animate({'top': '-24px'}, 300 );
	});

	// Service Icon Option	
	$(".link-block").hover(function(){
		$('.move-bg-icon',this).css("top","-100px");
		$('h2.move-item',this).css("left","-100px");
		$('p.move-item',this).css("bottom","-100px");
		$('.move-bg-icon',this).stop().animate({'top': '0'}, 300 );
		$('h2.move-item',this).stop().animate({'left': '0'}, 300 );
		$('p.move-item',this).stop().animate({'bottom': '0'}, 300 );
	}, function(){});	
	
	// Awards
	$(".award").hover(function(){
		$(this).stop().animate({'opacity': '1'}, 500 );
	}, function(){
		$(this).stop().animate({'opacity': '0.5'}, 500 );
	});	
	
	// Bootstrap Accordion
	$('.accordion-toggle').append($('<div class="marker"></div>'));
	$('.accordion').on('show', function (e) {
		 $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('target');
	});
	$('.accordion').on('hide', function (e) {
		$(this).find('.accordion-toggle').not($(e.target)).removeClass('target');
	});	

	// Bootstrap Tabs
	$('.tab-pane').append($('<div class="bottom-pattern-line"></div><div class="bottom-pattern-right"></div>'));	
	
	// Meet Our Doctors
	$(".link-img-bg").hover(function(){
		$(this).stop().animate({'opacity': '1'}, 500 );
	}, function(){
		$(this).stop().animate({'opacity': '0'}, 500 );
	});	

	// Price button
	$(".button-price").hover(function(){
		var obj = $(this).parent().parent().parent();
		obj.find('h3').stop().animate({'borderColor':'#368ccc','background-Color': '#368ccc','color':'#fff'}, 500 );
		obj.find('.price-td').stop().animate({'background-Color': '#368ccc','color':'#fff'}, 500 );		
		obj.find('.dollar,.cents,.time').stop().animate({'color':'#e7e4e4'}, 500 );
		obj.find('.number').stop().animate({'color':'#fff'}, 500 );
		$(this).stop().animate({'borderColor':'#368ccc','background-Color': '#368ccc','color':'#fff'}, 500 );
	}, function(){
		var obj = $(this).parent().parent().parent();
		obj.find('h3').animate({'borderColor':'#fff','background-Color': '#ededea','color':'#368ccc'}, 500 );
		obj.find('.price-td').animate({'background-Color': '#ededea','color':'#fff'}, 500 );
		obj.find('.dollar,.time').animate({'color':'#575757'}, 500 );
		obj.find('.cents,.number').animate({'color':'#368ccc'}, 500 );
		$(this).animate({'borderColor':'#fff','background-Color': '#ededea','color':'#368ccc'}, 500 );
	});		
	
	// Table odd	
	$(".column ul.odd").each(function(indx, element){
		$("li:odd",this).addClass("row-odd");  
	});

	// Carousel //
	$('.review-slider').carousel({
		interval: false,
		pause: 'hover'
	});
	is_carousel_working = false;
	
	//Next Item
	$('.review-slider .next-slide').on('click', function(){
		if(!is_carousel_working) {
			is_carousel_working = true;
			var obj = $(this).parent('.review-slider');
			var active_item = obj.find('.active');
			active_item.find('.md').fadeOut(150);
			var next_item = active_item.next('.item')
			if (next_item.length) {
				slider_bq_h = next_item.height();
				next_item.find('.blockquote').css("height", active_item.find('.blockquote').height() - 15);
			}
			else {
				var first_item = obj.find('.item:first-child');
				slider_bq_h = first_item.height();
				first_item.find('.blockquote').css("height", active_item.find('.blockquote').height() - 15);
			}
			obj.carousel('next');
		}
		return false;
	});
	
	//Prev Item
	$('.review-slider .prew-slide').on('click', function(){
		if(!is_carousel_working) {
			is_carousel_working = true;
			var obj = $(this).parent('.review-slider');
			var active_item = obj.find('.active');
			active_item.find('.md').fadeOut(150);
			var next_item = active_item.prev('.item')
			if (next_item.length) {
				slider_bq_h = next_item.height();
				next_item.find('.blockquote').css("height", active_item.find('.blockquote').height() - 15);
			}
			else {
				var first_item = obj.find('.item:last-child');
				slider_bq_h = first_item.height();
				first_item.find('.blockquote').css("height", active_item.find('.blockquote').height() - 15);
			}
			obj.carousel('prev');
		}
		return false;
	});
	
	$(".review-slider").on('slid', function(){
		is_carousel_working = false;
		var obj = $(this);
		obj.find('.active .blockquote').animate({height: slider_bq_h - 15}, 350);
		obj.find('.blockquote-line').animate({height: slider_bq_h + 50}, 100, function() {
			obj.find('.active .md').fadeIn(300);
		});
	});
	$(".review-slider").each(function(index, el){
		var active_item = $(el).find('.active');
		active_item.find('.md').css("display", "block");
		var h = active_item.height();
		active_item.find('.blockquote').css("height", h - 15);
		$(el).find('.blockquote-line').css("height", h + 50);
	});
	
	// select menu
	$('#selectMenu').change(function(){
		var href = '';
		$('option:selected', this).each(function(){
			href = $(this).attr('value');
			window.location.href = href;
		});ye
	});
	
	// timer
	$(function () {
		var austDay = new Date();
		austDay = new Date(austDay.getFullYear(), austDay.getMonth() + 1, 26);// (2015,01,01)
		$('#countdown').countdown({until: austDay});
		$('#year').text(austDay.getFullYear());
	});
	
	// contact form
	$("#ajax-contact-form").submit(function() {
	var str = $(this).serialize();
		$.ajax({
		type: "POST",
		url: "includes/contact-form.php",
		data: str,
		success: function(msg) {
			if(msg == 1) {
				result = '<div class="alert success fade in">Your message has been sent. Thank you!<a href="#" class="close-alert" data-dismiss="alert"></a></div>';
				$("#ajax-contact-form").hide();
			} else {result = msg;}
			$('#form-message').hide();
			$('#form-message').html(result);
			$('#form-message').fadeIn("slow");
			}
		});
	return false;
	});
});