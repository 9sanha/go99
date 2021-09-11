<!doctype html>
<html lang="en">
<!--부트 스크랩 컴포넌트 url: https://getbootstrap.com/docs/4.0/components/alerts/-->
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS 버전 바뀌면 이 코드 수시로 바꿔줘야 함-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>

    <title>왕초보 시작반 2주차 숙제 복습</title>

    <style>
        /*가운데 정렬*/
        .wrap {
            width: 600px;
            margin: auto;
            margin-top: 50px;
            margin-bottom: 50px;
        }
        .background-img{
            width: 600px;
            height: 300px;
            background-image: url("https://t1.daumcdn.net/cfile/tistory/99DA1E415F0CCDF60B");
            background-position: center;
            background-size: cover;
        }
        .text-ar{
            margin-top: 5px;
            font-size: 15px;
        }
        .price{
            font-size: 20px;
        }
        .form-floating{
            margin-top: 10px;
        }
        .buyInfoBox{
            margin-top: 20px;
        }
        .aa{
            width: 600px;
            margin: auto;
            margin-top: 10px;

        }
        .rate{
            font-size: 13px;
            color: cadetblue;
        }
    </style>
    <script>

        $(document).ready(function () {
            $.ajax({
                type: "GET",
                url: "https://api.manana.kr/exchange/rate.json",
                data: {},
                success: function (response) {
                    let nowRate = response[1]['rate'];
                    $('#rate-box').text(nowRate);
                }
            })
            order_listing();
        });

        function order_listing() {
            // 주문목록 보기 API 연결
            $.ajax({
                type: "GET",
                url: "/order",
                data: {},
                success: function (response) {
                    let list = response['orderList']
                    for(let i =0 ;i<list.length;i++){
                        let name = list[i]['name']
                        let address = list[i]['address']
                        let number = list[i]['number']
                        let quantity = list[i]['quantity']
                        let template = `
                            <tr>
                                <th scope="row">${name}</th>
                                <td>${quantity}</td>
                                <td>${address}</td>
                                <td>${number}</td>
                            </tr>
                        `
                        $('#orderlist').append(template)
                    }

                }
            })
        }

        function order() {
            // 주문하기 API 연결
            let name = $('#floatingName').val()
            let address = $('#floatingAddress').val()
            let number = $('#floatingNumber').val()
            let quantity = $('#selll').val()
            $.ajax({
                type: "POST",
                url: "/order",
                data: {
                    give_name:name,
                    give_address:address,
                    give_number:number,
                    give_quantity:quantity
                    },
                success: function (response) { // 성공하면
                    alert(response["msg"]);
                    window.location.reload()
                }
            })
        }
    </script>
</head>

<body>
<div class="wrap">
    <div class="background-img"></div>
    <h1>빗 팜<span class="price">가격:505050505000</span></h1>
    <div class="text-ar">
        이 빗은 사실 특별한 힘을 가지고 있습니다. 빗의 손잡이를 잡고 머리를 세게 내리치면 내리치는 힘에 비례해서 머리가 자라납니다. 정말 신기하죠?
    </div>
    <span class="rate" id="now-date"></span>
    <p class="rate">달러-원 환율: <span id="now-rate"></span></p>
    <div class="buyInfoBox"></div>
    <select class="form-select" aria-label="Default select example" id="selll">
        <option selected>수량을 선택하세요</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>
    <div class="form-floating mb-3">
        <input type="text" class="form-control" id="floatingName" placeholder="이름을 적으세요">
        <label for="floatingName">주문자 이름</label>
    </div>
    <div class="form-floating">
        <input type="text" class="form-control" id="floatingAddress" placeholder="주소도">
        <label for="floatingAddress">주소</label>
    </div>
    <div class="form-floating">
        <input type="text" class="form-control" id="floatingNumber" placeholder="번호도">
        <label for="floatingNumber">전화번호</label>
    </div>
    <button onclick=order() type="button" class="btn btn-secondary btn-lg aa">주문하기</button>



    <table class="table">
        <thead>
        <tr>
            <th scope="col">이름</th>
            <th scope="col">수량</th>
            <th scope="col">주소</th>
            <th scope="col">전화번호</th>
        </tr>
        </thead>
        <tbody id="orderlist">

        </tbody>
    </table>
</div>
</body>

</html>
