jQuery(function($){

    // header slide down menu(profile menu);
   
'use strict';
var MONTHS = ['Yanvar',
	'Fevral',
	'Mart',
	'Aprel',
	'May', 
	'Iyun',
	'Iyul',
	'Avgust',
	'Sentyabr',
	'Oktyabr',
	'Noyabr',
	'Dekabr'
	]
	var d = new Date();
	var s =d.getTime();
// var p = $( ".column-previous-paid" );
// var t = $( ".column-current-paid" ).offset();
// var z = $( ".column-current-debt" );
// var x  = z.offset().left+z.width();
// var position = p.offset();
// var w = p.width();
$('#result_list').prepend(`<thead><tr>


<th id="l" scope="col" colspan=3 class="column-previous-paid"> 
   <div class="text"></div>
   <div class="clear"></div>
</th>
<th id="k" scope="col" colspan=4 class="column-previous-paid">
${MONTHS[d.getMonth()-1]}
</th>
</th>
<th id="m" scope="col" colspan=4 class="column-previous-paid">
${MONTHS[d.getMonth()]}
</th>


</tr></thead>`);
$("#l").css({
	'color':'black',
	    'text-align': 'center',
      'background-color':'#ecf2f6',
       'border': '1px solid',
    'border-color': '#59677D',
    });
$("#m").css({
		'color':'black',

	    'text-align': 'center',
      'background-color':'#ecf2f6',
          'border': '1px solid',
    'border-color': '#59677D',
    });
$("#k").css({
		'color':'black',

	    'text-align': 'center',
      'background-color':'#ecf2f6',
            'border': '1px solid',
    'border-color': '#59677D',
    });
$( ".pages-wrapper" ).after( 	`<input type="submit" name="_save" class="default" value="Сохранить">`);
// $('#changelist-form').append();
// console.log(position.left, position.top,w, t.left, t.top);

$('input').keyup(function() {  
    var i=this.id;
	var id = i.split('-')[0];
	var sum1 = parseInt($('#'+id+'-0').text()) +parseInt($('#'+id+'-1').val())-parseInt($('#'+id+'-2').val())-parseInt($('#'+id+'-3').val());
    var sum2 = sum1+parseInt($('#'+id+'-5').val())-parseInt($('#'+id+'-6').val())-parseInt($('#'+id+'-7').val());
      var s  =  'topay-' + id;
  // console.log(id, sum1, sum2);
  if (isNaN(sum1) || isNaN(sum2)) {
    $('#total').text('Both inputs must be numbers');
  } else {          
    // console.log('dfs');
    $('#'+id+'-4').val(sum1);
    $('#'+id+'-8').val(sum2);
  }
});

});
