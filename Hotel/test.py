socket.on('rehome', function (id) {
          let matches = id.match(/(\d+)([A-Za-z]+)/);
          let remsg, roomid;  // 在 if 块外部声明变量

          // 获取id为remsg的元素
          let remsgElement = document.getElementById('remsg');
          let remsgContent = remsgElement.innerText || remsgElement.textContent;
          console.log(remsgElement);
          if (matches) {
              // 匹配到了，输出结果
              roomid = matches[1];
              remsg = matches[2];
          } else {
              // 没有匹配到
              console.log("未找到匹配的数字和字母");
          }

          if (remsg == "Y") {
            remsgContent += roomid + "室の客様は掃除OK<br>";
          } else {
            remsgContent += roomid + "室の客様は掃除NG";
          }

          remsgElement.innerHTML = remsgContent;
      });