<script>
    let hour = new Date().getHours()
    let min = new Date().getMinutes()
</script>

<header>
    <div class="info-bar">
      <div class="info-bar__time">{hour}:{min}</div>
      <div class="info-bar__icons">
        <img src="assets/chart-bar.svg" alt="chart-bar" />
        <img src="assets/wifi.svg" alt="wifi" />
        <img src="assets/bettery.svg" alt="bettery" />
      </div>
    </div>
    <div class="menu-bar">
      <div class="menu-bar__location">
        <div>역삼1동</div>
        <div class="menu-bar__location-icon">
          <img src="assets/arrow-down.svg" alt="bettery" />
        </div>
      </div>
      <div class="menu-bar__icons">
        <img src="assets/search.svg" alt="" />
        <img src="assets/menu.svg" alt="" />
        <img src="assets/alert.svg" alt="" />
      </div>
    </div>
  </header>

  <main>
    <a class="write-btn" href="#/write">+ 글쓰기</a>
  </main>

  <footer>
    <div class="footer-block">
      <div class="footer-icon">
        <div class="footer-icon__img">
          <img src="assets/home.svg" alt="" />
        </div>
        <div class="footer-icon__desc">홈</div>
      </div>
      <div class="footer-icon">
        <div class="footer-icon__img">
          <img src="assets/paper.svg" alt="" />
        </div>
        <div class="footer-icon__desc">동네생활</div>
      </div>
      <div class="footer-icon">
        <div class="footer-icon__img">
          <img src="assets/map.svg" alt="" />
        </div>
        <div class="footer-icon__desc">내 근처</div>
      </div>
      <div class="footer-icon">
        <div class="footer-icon__img">
          <img src="assets/chat.svg" alt="" />
        </div>
        <div class="footer-icon__desc">채팅</div>
      </div>
      <div class="footer-icon">
        <div class="footer-icon__img">
          <img src="assets/user.svg" alt="" />
        </div>
        <div class="footer-icon__desc">나의 당근</div>
      </div>
    </div>
  </footer>
  <div class="media-info-msg">화면 사이즈를 줄여주세요</div>

  <style>
    .info-bar__time {
        color: blue;
    }
  </style>