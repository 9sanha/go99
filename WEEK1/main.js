$(document).ready(function () {
    movie_listing('드라마')
})

function movie_listing(genre){
    $.ajax({
        type: "GET",
        url: `/genre?givegenre=${genre}`,
        data: {},
        success: function (response) {
            console.log(response)
            //기존 카드 지우는 코드
            let list = response['movieList']
            for(let i =0 ;i<list.length;i++){
                let img_url = list[i]['img_url']
                let title = list[i]['title']
                let grade = list[i]['grade']
                let genre=''
                for(let t = 0 ; t <list[i]['genre'].length;t++ ){
                    genre+= list[i]['genre'][t]
                    if (t!=list[i]['genre'].length){
                        genre+=', '
                    }
                }


                let template = `<div id="card" class="card mb-3" style="max-width: 400px;">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="${img_url}" class="img-fluid rounded-start" alt="...">
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 id="movie-title" class="card-title">영화 제목: ${title}</h5>
                    <p id="movie-grade" class="card-text">영화 평점: ${grade}</p>
                    <p id="movie-genre" class="card-text">영화 장르: ${genre}</p>
                    <p id="movie-open-day" class="card-text"><small class="text-muted">영화 개봉일</small></p>
                    <a class="btn btn-primary" href="#" role="button">Link</a>
                </div>
            </div>
        </div>
    </div>
                        `

                $('#card-list').append(template)
            }

        }
    })
}

function pass_genre(genre){
    console.log(genre)
    let give_genre=''
    switch (genre){
        case '1':
            give_genre='드라마'
            break
        case '2':
            give_genre='판타지'
            break
        case '3':
            give_genre='서부'
            break
        case '4':
            give_genre='공포'
            break
        case '5':
            give_genre='멜로/로맨스'
            break
        case '6':
            give_genre='모험'
            break
        case '7':
            give_genre='스릴러'
            break
        case '8':
            give_genre='느와르'
            break
        case '9':
            give_genre='컬트'
            break
        case '10':
            give_genre='다큐멘터리'
            break
        case '11':
            give_genre='코미디'
            break
        case '12':
            give_genre='가족'
            break
        case '13':
            give_genre='미스터리'
            break
        case '14':
            give_genre='전쟁'
            break
        case '15':
            give_genre='애니메이션'
            break
        case '16':
            give_genre='뮤지컬'
            break
        case '17':
            give_genre='SF'
            break
        case '18':
            give_genre='액션'
            break
        case '19':
            give_genre='무협'
            break
        case '20':
            give_genre='범죄'
            break
        case '21':
            give_genre='서스팬스'
            break
        case '22':
            give_genre='서사'
            break
        case '23':
            give_genre='블랙코미디'
            break
        case '24':
            give_genre='실험'
            break
        case '25':
            give_genre='공연실황'
            break
    }
    //give_genrefun(give_genre)
    movie_listing(give_genre)

}
