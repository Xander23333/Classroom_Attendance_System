head = "<table class=\"table table-condensed table-hover\" >"

function turntable(dic) {
	tex = ''
	for(cl in dic){
		tex += "<thead ><tr class=\"success\"><th>班级："+ cl +"</th><th></th></tr><tr><th>学号</th><th>姓名</th></tr></thead>" 
		tex +="<tbody>"
		for (id in dic[cl]){
			tex += "<tr> <td>"+id+"</td> <td>"+dic[cl][id]+"</td></tr> "
		}
		tex += "</tbody>"
	}
	return head+tex+"</table>"
}

function start(x) {
	setInterval(function() {
		$(function() {
			url = "rollcall.json";
			//					html无法访问到父目录的东西?
			$.getJSON(url, function(content) {
				$(".donenumber").text(content.donenumber);
				$(".undonenumber").text(content.undonenumber);
				$(".modal-body1").html(turntable(content.done));
				$(".modal-body2").html(turntable(content.undone));
			});
		});
		pieChart();
	}, x * 1000);
}