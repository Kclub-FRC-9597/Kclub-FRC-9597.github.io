<script>
	//监听页面滚动
	window.addEventListener('scroll',function(){
		//获取页面滚动的距离(Y轴)
		var navbar = document.getElementById("banner");
		//当距离大于100时执行动画并将导航栏设置为可见
		if(window.pageYOffset>100){
			console.log(">100");
			navbar.style.transform="translateY(0)";
			navbar.style.opacity=1;
		}else{
			//收起导航栏
			navbar.style.transform="translateY(-100%)";
			console.log("<100");
		}
	});
</script> 
