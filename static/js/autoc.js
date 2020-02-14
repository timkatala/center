// jQuery(function($){

//     // header slide down menu(profile menu);
   

// 	$("#search-box").on('propertychange input', function(e) {
//           e.preventDefault();

// 		$.ajax({
// 		type: 'POST',
// 		url :window.location.origin + '/uz/search/',
// 		data:'keyword='+$(this).val(),
// 		beforeSend: function(){
// 			$("#search-box").css("background","#FFF url(LoaderIcon.gif) no-repeat 165px");
// 		},
// 		success: function(data){
// 			$("#suggesstion-box").show();
// 			$("#suggesstion-box").html(data);
// 			$("#search-box").css("background","#FFF");
// 		}
// 		});
// 	});
    
// });
jQuery(function($){

    // header slide down menu(profile menu);
   
'use strict';
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
    // serch user on header menu;
    var sVal = '';
    $('#search-box').on('propertychange input', function(e) {
     e.preventDefault();


        sVal = $(this).val();

        var url = window.location.origin + '/uz/search/';                        
       if($('#my-list option').filter(function(){
        return this.value=== sVal;        
    }).length) {
        //send ajax request
                window.location = '/uz/admin/payment/student/?q='+sVal;
    }
           
     $.ajax({
     type: 'POST',
     url :window.location.origin + '/uz/search/',
                  data: { search:sVal },
                 
    
     success: function(data){
        // console.log(data);
         $("#search-results").html(data);
     }
     });

        
        
    });

  // $("[list='my-list']").on("input",  function() {
  //     console.log("Gf");

  //   window.location = $("#my-list option[value='"+$("[list='my-list']").val()+"']").find("a").attr("href");
  //       });


$('.topay').keyup(function() {  
    var i=this.id;
var id = i.split('-')[1];
      var input1 = parseInt($('#tochange-'+id).val());
      var s  =  'topay-' + id;
   var input2 = parseInt($('#'+s).val());
  console.log(id, input1, input2);
  if (isNaN(input1) || isNaN(input2)) {
    $('#total').text('Both inputs must be numbers');
  } else {          
    // console.log('dfs');
    $('#special-'+id).val('='+(input1 + input2));
  }
});


});

//To select country name
// function selectCountry(val) {
// $("#search-box").val(val);
// $("#suggesstion-box").hide();
// }




// jQuery(function($){
// 'use strict';
// $( "#search-user" ).autocomplete({
//     minLength: 1,
//     source: function(request, response) {
//         $.ajax({
//             url :window.location.origin + '/uz/search/',
//             data: { term: $("#search-user").val()},
//             dataType: "json",
//             type: "POST",
//             success: function(data) { 
//                 response($.map(data, function(obj) {
//                     return {
//                         label: obj.name,
//                         value: obj.name,
//                         // description: obj.description,
//                         id: obj.name // don't really need this unless you're using it elsewhere.
//                     };
//                 }));
//             }

//         });
//     }
// }).data( "autocomplete" )._renderItem = function( ul, item ) {
//     // Inside of _renderItem you can use any property that exists on each item that we built
//     // with $.map above */
//     return $("<li></li>")
//         .data("item.autocomplete", item)
//         .append("<a>" + item.label + "<br>" + item.value + "</a>")
//         .appendTo(ul);
// };

// });

// jQuery(function($){

//     // header slide down menu(profile menu);
   
// 'use strict';
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });
//     // serch user on header menu;
//     var sVal = '';
//     $('#search-user').on('propertychange input', function(e) {
//     	e.preventDefault();

//         console.log(123);

//         console.log( $(this).val() );
//         if( e.keyCode == 13 ) {
//             return false;
//         }
//         if($(this).val() !== '') {

//             sVal = $(this).val();

// 			var url = window.location.origin + '/uz/search/';                        
// 			console.log(url);
//             $.ajax({
//                 method: 'POST',
//                 url: url,
//                 data: { search:sVal },
//     //             headers: 
//     // {
//     //     'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
//     // }
//                 success: function(response) {
//                     console.log(response);
//                     $('.results').children().remove();
//                     $('.view-all').children().remove();
//                     if(response.success === 'ok') {
//                         console.log(response.data);
//                         for(var i = 0; i < response.data.length; i++) {
//                             $('.results')
//                                 .append(
//                                     '<a href="' + response.data[i].url +
//                                     '" class="rs-item"><span>' + response.data[i].username + '</span></a>'
//                                 );
//                         }
//                         /*
//                         if(response.count >= 2) {
//                             $('.view-all').append('<a href="' + response.url + '" class="rs-item">View all'
//                                 + '<span id="va_count">(' + response.count + ')</span></a>');
//                         }*/
//                         $('.results').parent().fadeIn(250);
//                     }
//                     else {
//                         $('.view-all').children().remove();
//                         $('.results').children().remove();
//                         $('.results').append('<div class="rs-item not-f">No results!</div>').parent().fadeIn(250);
//                     }
//                 }
//             });
//         }
//         else {
//             $('.view-all').children().remove();
//             $('.results').children().remove();
//             $('.results').parent().fadeOut(250);
//         }
//     });

//     $('#search-user').on('keydown', function(e) {
//         var keyCode = e.keyCode || e.which;
//         if (keyCode === 13) {
//             e.preventDefault();
//             return false;
//         }
//     })
//     .siblings('button[type=submit]').click(function(e) {
//         e.preventDefault();
//     });
// });

