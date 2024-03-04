<template>
  <TopBar />
  <div
    class="w-full text-left dark:bg-gray-700 mx-auto dark:text-white h-screen"
  >
    <div class="flex p-5 gap-x-10">
      <a href="https://www.google.com" class="text-2xl font-bold">Google</a>
      <div class="w-full flex flex-col gap-y-3">
        <input
          type="search"
          placeholder="search"
          class="w-full border rounded-full p-1 px-2"
        />
        <div class="flex gap-x-2 justify-start">
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Images
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Videos
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Download
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Compiler
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Code
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Learn
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Shopping
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            Online
          </button>
          <button class="border rounded-full px-2 hover:bg-gray-400">
            W3schools
          </button>
        </div>
      </div>
      <img
        src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D"
        class="border rounded-full h-10 w-10 object-contain"
        alt=""
      />
    </div>
    <hr class="mt-2" />
    <div
      class="w-full flex px-20 flex-col gap-y-3 items-start justify-center mt-1"
    >
      <div class="flex flex-col gap-y-2">
        <div class="flex items-center gap-x-1">
          <img
            src="https://chadura.com/static/images/chadura-blue.png"
            class="h-5 w-5 rounded-full"
            alt=""
          />
          <div class="flex flex-col">
            <p class="text-sm font-bold">Python</p>
            <a href="https://www.python.org" class="text-xs">www.Python.org</a>
          </div>
        </div>
        <div class="text-left">
          <a href="#" class="text-blue-500 text-xl">Welcome to Python</a>
          <p class="flex-wrap">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
            explicabo rerum atque nostrum! Vel corrupti, esse iusto voluptate
            sapiente odit.
          </p>
        </div>
      </div>

      <div class="flex flex-col gap-y-2">
        <div class="flex items-center gap-x-1">
          <img
            src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAACUCAMAAACtIJvYAAAAaVBMVEUAAAD////u7u7t7e3+/v79/f319fXz8/P4+Pjo6OgFBQXS0tIeHh7Ozs4kJCTi4uLb29u5ublkZGTHx8exsbFGRkZ6eno7OzsxMTGGhoZRUVFYWFgZGRmMjIympqa/v7+ZmZkQEBBvb2+Oi4YVAAATfElEQVR4nM1ciZKrKhANKIsxUaNmnxiT///Ix9Ld4Jblzq1bj6qpcgLiEXqn2xVzTXHbtLvW9jJRvsP9ngh3LRP7j+8Q7nee+n+U4lnGldRaM/NnZnMdqZs2gWmju1N3zaNpE+ln8h2rX6CS2uBJ7v35UNfXi2nXa10fzv29BCB/FVXyASozKm/662Y134pr3+TKgv43a+U7RHe+PBYQYXtczp0SUv05Kp7YhrfbpuIOvN3+LnTe798ACu3Y57S4YdrUXfNoWkLl2kr7Jm1bupZ4rQXj/fXdIg3b+tpnTGg5mmr+Gf5SrpLxYiBqv0rpYCn1vf4KEbbrjmsdLQYHupnsEHSspoSDqFxLkewSrmV7+SNMtu27AeEgqhE1Iyu9QQVrZW4XWffioUfPjD+3F2O6bBZV8seopOb9cfyU9YnkwnELl7wP3T8T6L36PaokWqv2NH7Cs81aJPuikmt/lQmCdWra55hXTzttn5HMoYql5EqZJrkWtknl/nPXQrn/zEXKqutw8uLQmLly+n/LErjKpKZNrM0KN4dieOslN0+RSkTP88/W7ho63skrw5LJeTDvz6E1fUJW9LxGJBnsGmepPuDvT6Yky9rDcCtv3E27wPkgrxgy2bxsV7oZbENxLr3ilcSPrbk7oBJckfTozUMM65a3wYLtG4Pql3qwH6x/p1K4/UmPZkNUiVIBsJ3LLInsBjLlJuWv9GAZz3bqDAVCRxu2aYyKy4p4o5RAzrKLefhSyl+s1X0dZvrppaaOiubXU1SJDt0Rk/URfa13+iUqR/PeEOIytddeckjBRB+BemYgUswgxpEpCwPD3g2oVtzLOUFLeTBWh/bT6uwZpjO7qLh/toyeDRplWQ8qfghzHBsRBEvCaPpG+7s5yiuUgyQftqju7LQx55z1jB58J0VZFgmpm5KRuNO0Eq3f7SmqVODdp8qTh59WRirpmumvZXsWXut091Y63p4hMdfwwCkqoUqk7kuMypBq0BL7UibfoSoDy9R8qBpSlEeXhEzVCSqut6MFBcKQWTCGTrn+ClUZ3qjXQ4XF7tiTs3QZVZLiZhWliplMqT7AquQLVIZH0zRlyA2M9mi1aQ2RkOCwgzJcxR6dGD5EZQfZLScZf3VLKqlDtyTrT0Zw+WkRVWrbakZPykBTm60IOtMpUIZa8cKxI5Uqkgyk4VmJs+xYUL9WALAtGdnHhOno2f5uhVI02iIRQB0rmQw2OJEkIE0X+gMjKUruK/LqPmMjRZYT2e65/ki2BxV3LCeel0SO790EC6jAsta4h2c28rx0RbCemn+CigyXSzb2BxONZvIV6fEVqrCH1dgflCVtyEF/gGoXKJFNvFSNumwrP0AlSMQ/07GXGqnw1urOWVQk+xskxGNlO6w5GFCRoWnUm/l5ga7IgzIsihu+s6hiY9JQKG7i+i7HVp8nevAXldS03w0LHTBIoFTYVOhgQkewkGV0h9QpytIjG3bY6E1D9KsFzASDVpZhosUIan3TaZUEz8uxKOrrTnN0XxelqFkau5RI8B0LW+SWMg1Syxpp2t4wr501EZXbpooFL9WiwhVZaa68nbws25HscvDJLiomHMMIsVmzur/QOLpcrwbtlsXMIJA7jWb7GBURfBeh0kPDe7V6lGIRFXuuRu3URqiQqi5m5s9RSZyKUEnRToI6TzZAFVt97XisnazRwKIC39qyzCiQNEdXyKK4LK1HJXkzdnldr4ytPklxGqlx9HnwKvXWyGIzguEPTI8iO5ooLtG+A35312h/1PYHowMHLu8RqaIQmu7QkZeqccCVsW4QWjzuLNOgWL+PF2Mkr8ahIHLy71Imu8ELb7rApOdYXgVyLpFTc8V1PgwK7Vsh4PYLHxHOsmz3ho7ChXyybkhPVyuoUd07VTLWOAlZ2p12ZNeMKBLfqR+T8ztUCTus5tpx559NqnWKyqhLxOynUkzNB6Pk16jSqpiZ55ZokJLYW05RkVS/p2QIqdskBrWqU2Qyzt/ZV6mhKyMH5HYiCNbnTOA7kT3wHHmpQskctHKNqspZmeVEgm2uhzyz0Q8ZLEgpyRYVQdFZ+9PMsH1eJkt1KN1T8G4gjkcOdqkieYV738hYeyuWnWeWf3/bVZyYLJZXIZZjvJnqPhcDL86liFg0CWraGIAgr7x0TjV0XMUkApn1c2RR7J+HriylUfdWzAKqRDobTWdVd6j3s/f1pfHlERVYdcho6DQCKtbD77maiYvqtl6KsZ/21+etvUMwct3u2v553c8Jb7/IrRJeOxMqa9WhdLiJGBXnsNL1fLRW689PI162g7d9xqjQwN8nMSqJbLDT8zHkavE537VTyfkMKmLDXYwK3ZqTtcadO4kxG5E6FxIk3fG5Wc8+7XVbb2p8LNj73hkl55ehCVyDl+qwcbjH2UCjaK1jMuDQJxN5f5gKsZft0OdmogvOEE/rN8LyYQ+DMx70IAp950BMT+J4AmTVGiNUp1nePYulk8G4FUXd5ZkU0SNOjkenJ3GoWXpNsh0V79Oz9eTUUmFoXSnqyO7dYRLlD+16OHR3G8ZX4JLjFOU8KgU0VEtChRaQNzwna0W2yFGQuWi0geT2tLlqb+fzAVXA4Xy+9W2VmQUSA3JmGFju5lFJsDiLilBh7MezxmStEiSKm+0amMCeRY2l7AesDQBhT8PBGY3PncF6OyysFZL2zi7WyrIYvOnVMwB4G+7aG+YZ0PddcgzmDFh0EK31LrLrEIDKDYLFMCJpeDdEaxGEM+CtZBAbXFwvvEBh+xtdyGcNq+siPh50PEgTE2cQPIJBoH7dNQDf2BgbnuP4u901ssPGPsOgUigiq0HMJpKicEMdM8PHPg5SF5r9bsHHUtTcgShKL0VRRF7V0vngLSIJjGJ8g8rPBFt0s3s8RSV5xA4GFYrIQ7qACu2f7neoej/kwmZRaYUwPCqMX7ZLZ6mouptfoRLA6ad0dge1RDoRDhUGsXOM1o5ZPwM7SfwKlYaIw6NShAp4xa8VyNmjIayVSDFiZZ3E6ERVY/SUIucs6tBRfFcHCzkhCzka5JhaawijrfM0mNHx84AdHltpo7UgSH5YOFHhscuOZs4xjeJiL7xUF1UjbyIJWwQW587nfvBJ7gesTqusdsb9ZHPn0pG+OafjTKcPPS+YVgemmc+TASY1/uiKVEGn41OCCBU6Gv1vUcGDbkuoOmRCu1ZHXLj5nKIEbf1O/BJV9wYVUopDBYR6V3MndYZIEHYjoo7Poh+Do38JouEgwOob0xU6YAaVRNKvKKNnlOnDPO88cjGXZjSKFM0lDcG0KLCMDpnNXtIVkDvTK9SaRTmbU2QvPaqf/EV61quoGp2lgoQ5Znw2p4iXYCWYhUJUJzvSa2/fUvxH+8GbCjrmBmFGikrjQWJ4B1jBJ5WKmalEmoDxWRpUMHZdbIpiY1vhrvz1xl7D7pgr12BQEQ2iMQXevtlEc+F1NGgTbi9wUAGvlhtUId3l/9L+t6j0/xCVWLH/ISqjnf9WCOHvNYuqfD/sHzeLCqXofbvNfdvaRtd54/2un9Z3bKNBdN14pl43447oOgc9VywNwgSMSq0w+a3IFIhiYQ/fwSI1Kk5pL2d+8nEHOqNMYkh9bX5wg7DD/QPTSjQ2+XCQdv/oYPNmBpXwlz8VH2YWpO4fa2OTxvEdlJfAMQ9i1mawg9BmcNOidt5zsKyHWRRG9oPG0WpFflozm2FnL8lmiPTgwCiIo7U8unukBwFVzZNkVg+SzcAMKkDYLubWoqP2O2+CUNkzeUQVeRNcQf/GoapfoHKeF9qiv0WFVp+e9bwoK+FpUaFZfltEBQPO7Jeo8O3kPCoy1a0/qDBytIgKVvb4W1S4KUuoihgVRq9mUdl5AxUSqkSJL1D5h2NcrZGU7jCIM5CpblClFOmrlIb4lRMmPrhkryvgh1S5jtTHr3yCro8FRzlF7m7FMX7lRJGfFk6+1hWDuyl+5cUgmp8lt14qBkN2cqGaA3OMKhU6PvRx4lAQpDcVcsHHgT27ZD4CCd7hWS3VmCBBaC9Fv0DFI1RtIM9ZVBCPeqYeFfxbgzKZRGvRvTzL36BCFqsXUAmKb3lUoJ9+yoW1whD9Vf0KVRSonkGlM6DeXHpUGvywXRpQAev7jDyAfap+hQoYYjtB5fkYRYG9x+YUoUo5YygoziOyh6IJwG7SYVbQNKcokZO7YZAG+XLM5LADrlHG7m2hmD1LRVFfaD7xUv2KAezeL6XzUuOSmE+8VCIDl7fFQgfWhP2EDfZnXjn80shZ2U78cB1v8BeyXSIxO2ZCVGGDYSkfOaHKcAvVAir0OMQElT2sUPEJ72xigWkoq11ge4oqBQ71CVEOFeblFNkCKkwLaQKLkusus6qqUCnttnnltJSQaoBK4QiXaDu1ZNCb9yaAO6Onc4C7not+GDZ5hnvsEFs6qLK86Z7746n4eTzwWHr9ePwUp+P+2Td5ScZ0dMJ4EZHNGNEVcqAPZvjqM4GZVWy+Mgxj5XvuKtBY2fS3y+KRN7Ticu53pTtuMiwGuHs2G0jCyN1R+Oozj7qPoM6EgshpbLTKtocvquIel2eTRafwuWe4UVSNwgqdfzigwkwWSoIdVzXCYj77ei5J4c2i1X2JxAw2zEi2S+jGw/LVkHCKbKHW8lVZ2QcNz9AhYWGMCr2bwzB7h2Ig/QKqv+RhQ7xwhIpS4XM2QMUxjeJRTulKyWR3XXrO+qfYX67Yfa0vx+LFGf4umaErhQHRy6gCVFKtSs9GFaCaZdMqPd9Ot1trBFQmmQKIKjXiKzccel7g0KMrBx3yIKUxtil0UGamhtd9wCL7BKuEpfkk2clOXjumZ9JbutPKF3sCu+vrudepc0mCzD2bloqc/JAvitkZNUzrrZb8ME32qPscTLFXdRPcGAOi3PbTStbHcxvLdso33OmZjF98rzvOq0Q+Uxx7Zqk9hP9cO4tmWs5aV4RKo1i3B4dTVLhYe+nnFeVs7snVzfWNzcBmimw35wxQKUzVsDkDMxm/SEA315P0w3mOF7o7+e40HBdjJH97bk/tqPTAVioMKkB9HViIRVq1MErMPHUlZgdcWCg78X5dnDkg01Ar4pICUqwqKppuyJj7O5MhWFxJ52xOKkApCfaUlUOCqh2tYerflpFJIeDuF6dLZMPcDPXv6gHz1BlHoH6D5ipAEyT4evBS18ZzHL7WM/3Cm6B0FuPk2nLQZiCPT0g1pwxQxbLdowo1A1F75kwB1SIJ3L9AhRE+e1brCSefS7Vt2CIqPc3NLRopcaMELtbpG1RIC3nwJpuJcD3oV5Uvckjj+53z1jCpLCqC+DTOQAU8NxadxLJ2iGtP+QqjjF+wVQcnFbdk+H0Gcob2yYDaZ85Sca2ogKccxFNlNiiizuWo8iWJHxsVJzn5y8dhVdSjRsAH3p2rtUR/sMctYvFjLbaIzW2qy+sKUEnK+CDIxyHPHOUSWP3vpCjD7OaiGm6RvQw15M6h49EGT1ApTqR11hNU9O4+6+ktKpyro0RiREUFK6u9T6B6iYqrUGd5lnyMijDv3qNKqLyn0KNCLkY2la8BeF8BKnKSv4c4zcY7biTSsreoFNU8WD8zRqXCJwAeYNW8r0vdESy/UVA45a+RSG0aZ7pcUWXFBg2Vw6I3pYh417Nxz7kKUBUV5lxKrQYVoJIWoGPYYQQt/MbTkLNPubGrJKUKUNeRBdNmx8SrCtD4RCWWD0Wuo6rGKK5kHA81K0VRXkXwYVpg/aiMomWzp0fz3xxIWPTpkU7EoUKzRUjw13lUINsFqfrRt3eiqduYbiJmWPoSgm6D137AGAjMi2Vuq7NYRBVV0pcsIhwdVec/duwLVG5Ueg+wTtsBqkB2O7aIimr+OhFNy6Iar8edvUPlMsxCrprlhlD9u3qcpb8dKANtJMhSGaMyVIIa0/IfodLqHIy+UyNDwXKEytHVNC6E1yL+kMVxx0JKkaba8b3/P64+c4NI2D64QJdUiHtkKVwyNveFIqgAHWnnOKqmVGxu1TnSh1lUkqUHyee0My7mo0EGV2kVW90HOeX8F9o5jkAqPfgK0K1C+gieiT1KmKLqiaiAPHhaDaI6HdIN/5PvFOk8NgPXtiLUc3goq231BBW9i/fDlZTlLQ7E7WPf+U++U8T04B3X5y3zpdwJMVOjR6joUwlHiMBszwPP5gzL82KtXtCVbenEM7zsEvu9jSC1NobgYlRBuedunlGU6djo+Vy1mK7ef8GLRZ95cO10dq4YSS1ji4QTk5QUjZVmuhmHjHrOXn0lDHhwZocncVFdPkeRmc25zTR92OWUYe4HZ6E8vkt2k0DFE2zY2cxM9l62DyKQhlamn7+qb/TbJYM8GUmO7urxnH4A665nI5Af68Hpl/Hui0FIu1qQS7NdiAradr0L+fe/1yfaV7h8Ww57163UxGSfonpJV+g763z8ka0P2+lQWdOJpn2LKjIBobrEn/3LuAOMVK511b3Yo4V2bEtjbknINYhMzsgOxsoWPqwAXZZXbJhPLMrzFycmP9dzJqyuTMZeKvtTPTj1Uu3tSvC8vXxSfba+7HKJ5LH0vb4//zLe+Iucyoyp+uf1tFRN+Dhdn32OioX/G1RAtbJsuu45jvefnl3XVImNNIt/iwoTC6TPF1ElJCdWGRYNR0z2r1FZ35l4BRgruvuPUf0H4U0ygDavYH4AAAAASUVORK5CYII="
            class="h-5 w-5 rounded-full"
            alt=""
          />
          <div class="flex flex-col">
            <p class="text-sm font-bold">Python</p>
            <a href="https://www.python.org" class="text-xs">www.Python.org</a>
          </div>
        </div>
        <div class="text-left">
          <a href="" class="text-blue-500 text-xl">Learn Python here</a>
          <p class="flex-wrap">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
            explicabo rerum atque nostrum! Vel corrupti, esse iusto voluptate
            sapiente odit.
          </p>
        </div>
      </div>

      <div class="flex flex-col gap-y-2">
        <div class="flex items-center gap-x-1">
          <img
            src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoGBxESExYTExIWGBYRExgSFhgWExYaGBgYFhIYGRYYFhgaHysiGhwoHxYWIzQjKCwuMjExGSI3PDcwOyswMS4BCwsLDw4PHRERHDAfISEwMDAuLjAuMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMP/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABQYDBAcCAf/EAD0QAAIBAgIGCAMGBQQDAAAAAAABAgMRBCEFEjFBcYEGEyIyUWGRoXKxwSNCUoLR8ENikrLhBzPC8RQVc//EABsBAQADAQEBAQAAAAAAAAAAAAADBAUCAQYH/8QAMBEAAgIBAwEGBAcBAQEAAAAAAAECAxEEEiExBUFRgZGhYXGx0RMVIjLB4fAUQgb/2gAMAwEAAhEDEQA/AOzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGvUtb1OLLFXHcz1LJmB8R9OzwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjXndv0NqtO0WzQuZ2vn0h5ktUe83cNO8eGRmNLBzs7eJulnTT31r4cHE1hgAFg5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB8bANXHT2Lmap9qVNZt+OzhuPNzGulvm5FuEcLB9jKzv4EnF3V/Eirm9gZ3jbwLGjliTj4nF0eMmyADRK4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABjrVowTlJ2SIDH6VlUyj2Y+74/oR2Wxh1OZSSJXF6UpwyXafgvqyu1NPVqtRxi1GCvdJZtLxb+ljVx2KjTg5N2yy4kLofS66/q7WU4ZN7dZO6Xpcpzd9tU3BdE35d57p823Rj3dX5F0wFW6t+H5Gzch8PW1ZJ8nwJW5n6Z7oYfd/katsMS+Z6uaGm4SdNyi2pU3rXTadt+zy+RunmaTTT2NWfMtJYZDOG+Lj4kfojTdXUV5a1nZ62fvtJvC6Ypyyl2X57PUomGxcqFWpSkr6suDstj5polKGJjPY+W8n32VvrlGRGxrhl3R9KvgNJTpZbY/hf08Cw4XExqR1ou/wA15MtV2qfwZPGSkZwASnQAAAAAAAAAAAAAAAAAAAAAMdWooptuySu2ZCt6fx2vLq4vswefnL/BxOW1ZOZy2rJh0jpB1ZeEV3V9X5kVjMaoZLOXy4nnHYrUVl3ns8vMz9G9Buu+sqXVNPnN70vLxZUjBzeWVMuUsLqR9PRVXEJzvq04pynUlsSis0l95+xV8enGUakMnFpp701K8bnTum+LjRw3VQSXWtU0lklBZy9lbmc6rU9aLXj+0fT9k6ZKqUn38eRsaClQi5d7LbgcWqtONRbJxT4PeuTuiX0fW1o23xy5bijdDsfZyoSeavUiudpL1s+bLThMRqST3bHwPj9Rpv8Ak1Uq+7u+T5Rpyjvhx1JapUsfKdVMx4p7DCpHXKZXUE1k3f8A09CvfXgtdbJxylZq2b387le0voCrh+2nrQX3ks4/Et3HYWTAV7ST8cnzJlovVpSiZepoW7wyc+wePv2Zbdz8ePmSWDxcqUtaPNbmvBnjpR0e6u9akuxtnFfd/mXl5biN0fi9bsvatnmiKVbi8oofqg8Mv2FxEakVKOx+z3pmcqehsf1U7N9meT8vBlsLMJbkWoT3IAA7OwAAAAAAAAAAAAAAAAADT0riuqpylv2R4v8Ad+RT6lRJNvdmyY6VV7yjD8K1nxeS+T9Ss6Tq5KPjm+CIZrdIp3z5x4HrReCliayjsT7Un+GK/aXM6HRoxhFQirRirJLckQfQjA6lHrGu1Vd/yrKP1fMmcdilSpzqS2Qi5ei2EkI9yJqIYjnvZQunWO63EOC2UY6n5nnL6LkV9oy1qjnJylm5NyfFu7NXGz1YPxeS5n19NaqrUPBf73Nit7YpEPPGOliI1o7pXt4rZJc1f1Og0qqlFSi7qSTT8U1dHPMTTvHhmWroZKpLDJyXYhUlShLxslK3LWty8j5vtzTb4q7vXD+T+zLGms/VtfeWrA19em0+9Sdnw+6/T5Hu5FYfEdXVi33Z/Zy591+vzJOWWXgYiWVkllDbJrzM1CpZ8SxYSprRT8rPiirXJvQeIunHn+v0LNPDwUtZXmO7wJOSurPfkc+6SaMeGrdnuT7cPLPOPL5NHQyI6U4HrqErLtU/tI+N47VzV0WGsoyLobo/FFWoVtaKfjt47y2dH8Z1lKzfah2Xw3P9+BRNGVc3HxzRYejeMUK6g5L7RONr71mvk/UjisSK1M8SXxLcDzKViPxWnsNT71aN1ui9Z+kbkqWehoRhKbxFZ+RJAq+L6bUl3KU5ecrRX1fsTGgdI/8AkUY1bWcrppO6TjJp2fI7cJRWWia3S3VRU5xwnwSAAOCuAAAAAAAAAAAAUvTlXWr1H4S1f6Ul9Cv45uVSy25RXF/9kvj5Xqz+OX9zIzBrWxMF41of3o5UTMm8v5s6XhqKhCMFshFRXJWK30/x2rSjSTzqS1n8MLP5uPoWk5t0txvW4ibXdp/Zx/Ltfrcv9n1b7k30jz9jVjwyHaI3SdS8lH8K92ScnbN7syEqS1m34u59BN8FhSPB1vRvR9UsBTw6XbjDXf8A9H2pe7a4HPuhOjOvxdKLV40310+EGmvWWr7nYzF7SmpYr82czscWsdVyc3xENaLj4r3N/RuK62nGT7y7EviW/mrMy9J8H1VVtd2r21x+8vXPmQ2Ar9XWcX3a39273uuZgxhh4N7KtqVkfn9ycubOjMRqTT3X/wCzTuNYkSwQSipJouU5pZtpLzI/E6fw0L3qp+Ue0/Yoekqs1WlGU5SjNKcVKTaV9yvsV75GNssIjp7JjJKU5+i/30NepQfWSan2NeWqtXPVu9W+eTtYy0ZaklOLalF3T8Gt4Z8ZLGK8C3T2To6ukMv48/0ZMXjatT/cqSl8Um16bDXZ6Ziq1FFXZYiacUorC4PNepqq/pxL1/pzJvCLyqzXun9Tm9eq5P5I6b0BoauDh/PKc+Tk7P0SI73lGZ2w1/zpfFfRlhABVPmQAAAAAAAAAAACgaSVqtReFSX9zIqhU1MRCX4asHy1kyV6WOcMTOMYN66jNWTe1WeS80yKnoPFVXfs001tk7PkldnspwgszaXmZv4dkptQi3hnR9NYzqaNSpvjHL4nlH3aOVVMVBbZXe+2Zd9ORWKpQp1JuKi1KWq125KNt6yV22aGH0FhIbKcZPxm9b2eR3pu2NNpoPrKT8P78zajppvrwUrGYqc1q0qcpOWWUXJ+kUYqPR7G1Puai/nko+yu/Y6NVtGNoWS/lsvZGuVdT/8AR2yeK4JfPn6YRdq0i6tmh0LwTwCqSerOpW1VfO0YxTyW95tu+W4mcRpetP7+r8Kt77TTZ8Mi3W33S3Tl18OPoWY6apPO0galepGq1UnKTvq3lJvg8z7pGF43W2LuZtO4fZNfC/ozDQqa0c+DNPTy/EimaNeMEvo/FdZTUt+yXFbf15me5X9D4jqqjpvZN257nzX0J25aUSvOG14NDTtPsxqLbSln8Mn+tvU1rkrWpqUXF7JJx9UViljJpOLSTg3B8U7HWME9EuNpIMxVasVtaNGdeT2yZiZImWMmzVxv4Vzf6GpKTbu2GeqNKUpKMYuTk7JJXbfkjtM9ye8DhJ1qkKcF2pyUV5X2t+SV3yOxYHCxpU4U4rs04RguEVZfIr/Qzoz/AOMusqJOrJWS26kXa6v+J73y42gisnnhHzXaWrV01GH7Y+77wACMzQAAAAAAAYcTiFBXe3cvE5lJRW6XCR6ll4R6q1YxV5OxH19It5RVvN7TWrVXJ3b/AMcDG2Y92vnN4hwvcuQoS5lyeMVVltbu3lc0pMyV9J0o5a934R7T9jUnpO/doSfxWiZ86pTecl6uLxwjMfLGrLG13sjTj6tmGcq8tta3wq3yO46f4k6jIkHB+Br1MRTjtnFfmTfojQngr96cpcX+oWBprdfmTx00e9kir8WZqulKS2Nvgv1sa8tLt92nfj/gyKhBbIr0PRYjTWu7JIoI0cRVrVE42STXh+pHYJThNqT25Nee4nWRukaHaUl97Ln+/kXKsRf6Vgljx0MGkYbJLdl+jJvRuL62mpb1lLiv3cipU5atpxlHWX3otX81dZmDReKdGpqvuy7L+j/fiaijlZXed2Q3RyiyNlc01R1K7e6tHW/Msn9HzLDcjtPYfXp3W2nLWv5XtL9eQdeUU52/gxdmM7U3hELY3NHaGr179VTbSdm8kk/Nt+ZrQi20krttJK2bbySXmdU6N6MWHoQp/etrTfjKW302cjmS2IyY9vytbVdeEu9vPt/ZVNH/AOn1V2depGK3qn2pf1SSS9GWvQ+gcPhl9nDtNWc5ZzfPcvJZEoCJybILtZdcsTlx4dEAAeFYAAAAAAAAAELjK+tJtvJbOBKYuVoSfkVjEVtbgjI7Utxth5lzSVbm2fa+MeyC5v6I0qtPW77cuLy/pWRsQozl3Yt8ItmaGiq0v4bXFpGdXGyX7U/JGinXDq0jQUUtiS4ISJR6Cmk5TnGKSu3m7JbXsKbW6RSfcgrbnJvZuyRf0/Zupu/bH1aRxPXUQ6y+pOM8srGL09Ws3rJeForbzuQ1bH1p96rN/mdvRZGpDsK7/wByS9X9iL80rf7U/ZHQKdOU3aKcn4RV37G3S0LXl/Da+JpHP9HutRlGdOUoz260XmuPl5PIvOiOnzSUcRDW/nprP80H9PQ6fZm18Pd7FH89Tk4pJfHqSFLovVfenBcLv9DbpdFaf3qknwSX6m3gukWErdyvC7+7J6sv6ZWZIqaexr1OVRGPGDv8wumsqXoR9DQWHj/Dv8Tb9thuUcNCHdhFcIpfIytrxNDG6cw1L/crQT8NZOX9KzJIx8EV52yazOXqzR6ZaM62jrxXbpXkvFxt2l9eRzfHwutZbtvAt+m/9QYqLWGhrPZr1MorzUVm+dio0a+urtK93dJWW17F4F6iDxta+Rr9ia+ubemzz1X8r+fUlNC43rIarfahlxW5m9JJpp7GrPmVWjWdGopLd7xe1FmpVVJKSd1JXRKo4Ne2tJ/Bm/0G6OvXdeqsoNqmn95rJ1OHh/hF5IHoli9aEqb2wd18L/zcnijbne8nyEtOtPJ1ruf+9gACM8AAAAAAAAAAAAMdWmpJpq6e1HiGFhHZCK4JGcHO1Zzg9yfD6AdHhC9L8UoYeUd9X7Pk+97ZcyhrCU/wL0LF0xxevW1E8qSt+aVm/axWdIYnVVl3n7I3dFXspT8eTG1Frnc4x7uPuaOPlFyskrR8EtpI6B6L1sTTnUhqxUco610py3pNbLePjzHRno7Uxc98aUX25/8AGHjL5HUMJhoUoRpwioxgrRS3Ih1eq2foj1+hdpq3R56HKno+pQbjVg4y8Gt3k9j5HipQi/LgdXxWFp1Y6tSEZJ7pJMgMf0JpSzpVJQfg+1H9V6levVQaxNYK9mikuYc/U5/PCPxT4iFOpHY2uErFnxPQ7FR7qhNfyys/SSXzNOfR/Fr+BLlZ/JlhSql0kvX7lV1WJ8xfp9iElCrLa2+Mr/UQwj8kTUNAYt/wJc0l82bWH6IYuW2MYfHNfKNz1uqPWS9fsFVZLpF+hARw0d+fEw4ehUc1CEJSk9kYpttW22XzL5gehEFnVquX8sFqrm3d/IsOB0fSpK1OnGPjZZvi9r5lezU1r9nL9i7pqLq7I2J7XF5Xj9jkOkMNJXi01KLaae1NbUzJoLH6r6uTyk+z5Pw5/MvvTDo31y62kvtYrtL8aX/Lw9DmeOouMndNZ2aas01ua3FiuUbY7l1XVH6JptRDV1ZXXvXh/RfejuM1K0c8p/Zvm8vexdzk2htI9ZHVb7cPdbpHTdE4rrKUJ73HP4llL3uVNXXjEkYfa1LjJT8n/HsbgAKRkAAAAAAAAAAAAAAAAw4quqcJTlshFyfJGY8VIKSs0mntTV0PmePOODmOIxNSrN9XCVSpNtvUi5JN55tEpoXoNUk9fEy1Vt1Iu838UtkeV+KL1SpqKtFJLwSsey9ZrpyWIravcp0aKNfLeWYcNh4U4qEIqMYqyUVZIzAFEugAAAAAAAAAAAAr/SPorRxSbXYqNd5LveGut/HaWAHUJyg8xeCSq2dUt8HhnG9J9GsbhJa3Vyai8pQTnHnZXS4pF0/080uqkZU3lJdvV3rYpW8r2fMuBgjhoKWsoRUtl1FX9SxPVOdeyS8y/f2k9RT+HZFZ8Vx7GcAFUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//2Q=="
            class="h-5 w-5 rounded-full"
            alt=""
          />
          <div class="flex flex-col">
            <p class="text-sm font-bold">Python</p>
            <a href="https://www.python.org" class="text-xs">www.Python.org</a>
          </div>
        </div>
        <div class="text-left">
          <a href="#" class="text-blue-500 text-xl">Welcome to Python</a>
          <p class="flex-wrap">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
            explicabo rerum atque nostrum! Vel corrupti, esse iusto voluptate
            sapiente odit.
          </p>
        </div>
      </div>

      <div class="flex flex-col gap-y-2">
        <div class="flex items-center gap-x-1">
          <img
            src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAADhCAMAAADmr0l2AAAA/FBMVEX////+uQAAg//m5eXl5OTn5ubk4+P7+/vr6ur19fXz8vLv7u78/Pz4+Pjt7Oz09PT/tgAAfP8Afv8Aev//tADm5+vk6fLq5+T+ugAAdv///fnk5+33+v/v8vjv6uP0+f/0z4nu2bX18u799eX5xVg0kP/q3svv2K7z0JD+8dnY4en3x2f8vCT9xUzq7vb++vD/5LdAlv6Bsfiawv7/2pbw057w6Nj86MX90Xj5wk2szf5zq/nzy37+wDj8ymSevvDE2/7j7v9lpv796MEkiv/K1+xQnP6/2P/s2rzU5f/8vjD01JqRvP7R2uurx+7zzYR4sP2SufTwz5mqy/5NStN9AAAgAElEQVR4nMVdeV/iPBAuloocQoQe2AtF5FgQ8EDQxftccXX33e//Xd4cPdI2vYBd+8f2Z7SzmSYz8+TJZMpxHLfNC/w2vGcFvghvZV4Q4C3PC9kcx5VgawH+uCUIW/BWgK0ljstlBUGHP5rtdme8eDBga1BQEf5IBNmtQUE+8U3z6ebX/eHx8f3JS4PjeEcQQ3yyfnLLPVjStPZidgVEAMTBOKQHSyh4+lirVjfQVa3uPr+YynoUzPJZ9OAmbz3I4wdhaw6J47P4QZ7HD8IfOU4d9zMAgEwmAwYd3AN+kxIkSZqBWiWiYECQYAnCCpJWgefL3KmlnHVVa49PZjEoPnk/kYLb29uVYrGYh3d4K8BbAd6tG9VatFsNY9rCuiH1wMIw3EfyxaLR0A+mk729fv/sbPFqFnXdL94SZLXCR4oV3NqUD2sb/qv2vemKT9dPq0ccz2fx6yAaw9exmcMvibyObNZ625vobcNWnVvULe2gfn0VviTYmsdvkDe43uIoA6ctfAHoHzh9+/u8QcQLTPHW24YD9MM7fPYoHvPKJhm2VP3EswKLF9LYiyQsgKve26tsWQZSUJLb87ro/Nb5KzA/SGAv3I/g8BEND1e06xQjyMmdjKsAWGgSsgxrBNXJAAS0w+Moiv1R3AgqQ9bwEQ2flZVGMPncNs6PKPXezhvuL43yp087pFf94np+dnY27nS7zRgbVA/D9NvY2DltrmKDib2T3BXd/ot7Mp6X2Plxqkc9qFv9ujvtcYamafBvdEmSiCA+1Iue7oQruFH7KazgRRPHF3r4Mj2ZGB604DI3pieuOJg9mDIJE6695KLtRQ8xQHuSmkvHQQUruJkljiq7SaZ5FvcL/lgirfDBHj39WnCaZzeRgjwvv1JeFVxMDvAjlr1ks5agnCPIsRcivoRb30Mt0BpCZTNhPx27hj/Cm/rBZa2/3ozqjPZKT8+u7MpQr0VHuxaO+URyqs4okerBIXx3BUX2k35p2Mk0vycKE40ObWLToTML5LFlfEB8mwjykrCq+RQ5Q+H1uGSYULRHOMlsiw2HVWNq/AYHyLNgcZLQEq3B6/c4CfubZWBV8yR6hm5s7N5RglLAP/PkmPP6XBas0in9wFXF8cTGq+1yzpq633lHuvS816Wrz3EK7lyq8f1kwL/CzjNxMrwPDdFBWaLsD1xUyADB6G6FDVCfwGHLkmELCEoUlKOCoG2ESmw/WfDvsnYfGya4NhUDWlzFcr+83MeLifpiGGp4Se1FfYxV8LuyRJjguMfqSewIqgNaP+vNwPUgDovgU9Cw4UWO4GbcCMYreG8uM4KXtervOBscttwo1xrac7tYHADUYOr0jE9sgz7TacYr+GspG4TG+xLqRcl4awtXvyPXO0kD5Do7MnoklyXLJZ7pRbNJvGgCGwz1ouHwj4POuXbHiIM0rDJdAxy401yG81NswQU7hnvWcml5/qQZ70VfGHYdA/+4IYyuu/BPQmAVfgfDIzcAjhyEgPyLOIbvK0scKkFtUAAxRwvJkFcM8TZe8PI+JEPbS/N3kjgY1U8mkkGv7ZgjTiYEVkluBBTbko3PNNR6rhEsamnlw2eYk+ntT7rz6+vWdX/vv+kIxpswWNUMW+y6l5ke/v2pIdtVIsOE5hrgwsVnCgz3I4laTXjmJSIT2529i4GIqQvCTMEVVOZ6osgGczpVuDgTPDFTrya+VfHUJgqGwCrXw4ALd50lX4tH2I7d9aDjWSRZmJ5dWISb/wLi0URlO4TTuNWEkBb+jY6RyJrBR63oDbebBXelfC5eeMCW/Yje0HvdI7Zujo5gdmAwXHo+UsHqfTMt/BsReHusRrJqzgCK+5LLdcyvZJ5CQ5iTge9V7fQzQcqJMYz9g2BQVn5HruiHXEr4Z95gq67+bkayanW7Vy2Zcr8D1YOGoGVIcnPcihw53yiWJL93N4/Dx3Dnt8qlg3+WfnBqlwOsmgurjKkzgKYLqyrq1GKrHNQmdZJrR1TMdGQfrMo2IiaomRL+qZZ+G8eml1Ure3BPY2bT13PDw1aVt90ZbwzbMy/hhDwmotRQgKnX62hSOt7U/bNWM0/kbVuwqvkUMoTVY9X+T9n9LPhbmyeWfnCR5WXVvLCq4XRHYbFVhAxdDJDdEbUyV61+dzGe9nrnpoQCgs2qme32dHLWqlNqgsyr5l2cKj+ZzDZe0KWBf4pwbNtzNZpV69kDuKcxt8+kRu8axTqx3potOu1zpIomSTrTXlCrrLU7Z1eipSRidrz0gnQcjPe7700uHfx72bDfE2JyLAX9yxA8oW0fCpTgQhI+qE3q4tF88XqOXJwhJVsuoXF93cOjngHXsp+FvtzwONNq7fCnGbUaywaXS/fuS9ppIBfvY9X0fcXCeHLL0m/GYqu2eoupKcsSR2PRTRZqY8Gq0eQKbc9ceSm+0qai/Dms7eARqFZ3as+3DEFRrNroNzXNq+8mY/OlN5CtWSDbLrQXtllZcCdOytUEJ8nmoi6CgSB5pz2vcneXv56Pj4/v318kk7GMjwoTt4f0BKjq9uYLtc5SwUwjFiso1gwdcKzNyqC/CVkPhsEq3uCmLbFuMgSZpokMrxkmiMWqCUrz1ru9uHNq9ZPGPfqR2DUsNGRajOBCZ7BVNFRaYkVPgoyun7cyChNspRXfLN/4d08frV/STkabAzC2uQ4rzIsHWQZb5ex6Cnw2npOJgFW9lkJvdfnFZ2PE41mhmE+/AiGm9qQQQRw1zdvQ8Ke2vTwAa4aGZVmELJfSsmqv0gp2jYz0x/tjLRBBd05MOgnBejNoRk5t9zsGBMUw+UZ3BLMJRjCOVWOO4GbsCDZN89vL942gdgj+jGxBrg0OPxEm2S+WCe7ZJwruWzMeQSWEhirbAdRWLpa9RmK3MmFVSKv1CGsLE1tbDonP5XJNeKnwasq3p/cbVkwJKqg5/bS9aJE/F7FCEvFOkqWgyU75INPJ70UZKR9JWLWCoqC5pkL3idYNpiKgYat8+/at0WgM4W0I7/Am393dfXxc3pz+un+sQt3Cd72fFLefdhyUL7BC0CSIgq9YwbocnrRj2csKrJqimIjQvXt6uTk9/fX9/vn48RCOCrxqNftWc2+4tYqvMNWIg/kwg0kIRbIDARaSZS8kDl7ILHsJLHgZ9uKELxYLDYcMhrq7j5tfz4cbu3av47i1hNfupenpJ0FDJUIQgjMHVuEfP0N2Tp0dXjar5uAzBqwqK6YyfHm/f9yNmmXLX3D86H5aYUKYig7ytKbTFfpxHJ6Mt0SYEOCwNV7enyMNaMWremuyctWIBcLryHEIaL2LokZI9gKTVYuEVYopvLwf7oY4vjWp9/hTYeaqndsMb123/LOOAqF4TkMlNoflA1AhsEpVhzfP1b+q3AZaHuebvn5aTmbu8C/kbcMxQNsSwOSTBOV4WFX8eGYF5DVftd9mNiRXzWVL9iXLiowrHAZjw0QsrCpw+ulGFC24LvUOZTMsV80h0FCcsFffZ7BRSDSCUbBKMIcnf3tmoqta/YOjECtXLT/su5zXtW7vJsIFE8CwygOgyn585mvNu4/A1qJqnPyDublR3f0uNYusfmIvqtGUngOroGcFo8ReNBv0okVeMf/8tXjgUe/+Dk3F0Fy1Ns1s9ooWrIJoDSq4Shw0b/+F7VVrUL3InG39P1rBT8MGxvKbSO0jOG9mkzGCTHwm3cfu+62u3c7Gbwlj9JB+IjLMaNFTNOPuJk7FdkgOGIXa/Du8FmrLmh9/fXZWa9Xvt00uIlcNhwmhWKf1QzSavfo+6khLhgk1+5eHr1qtPZ7cQlwbn9LMmyKtIIKjtmc5X0gR68EoVu12468NH1x21HYev9/ccVzsUQXCqr36spF1C4nlt41z6HPzvs3KbeuXhdDWbfV99+/oVtt4PLw/uXwajppNBzFa/ym7n8jJjH0KTqS4HLAYVi37/HemZ/VDQ+LhajJhrprFqp35dvfqWpKzS+Fh4i7B9FxqeVv9UJY62jPzKQiHMPEIMli12+jhgxZUqx1+f79Jr2Htm5clYGy+BEewWKSzfawh1G18Vi5j1Fa2WTWCz0irD7WVy/gR9TTc/JB7eLw/vb0rN5uj+OSY4PPoPy2XrR5RoDCinyitPKAgONOicsAiWbVfYSdYoOt7Pv3QTLLhnm3+ST+Ch9hJJ85Vs1k1re5XMCMq1oTm2fGFp1m1LB0Hn1nYDCq3cY/cuqo49qLep1aw+p2mQbJ0rlpEP3leGwQUzLTk2PjCiINFjpEsAeHG/eVPE++FUbzoKP0AwgVRcATj+0noJf8QjqPPI7BZtdyhv9fV2uH7Dwg3vIJQZ+7Sm+DOk5L23ARh1RgKZsBB+jDR8OpX3ak+3xi+xb0j6DL9OqMqLXkClKVg5krnI88EBVk13RP+qtX7D8kzLzc90+l7+il6bC5zdimf169ZCoK+AXEPvCzcUyCgCKMh0lrI0/isYDxS++O158uKigmufJ5+xIFVamr1NqonUGDFLyhfKEb2EzmZOUvBjPiJJjSTk2FS9878hLHutAH9ZVQCufIz/Qyt3XLhm6rh/RQEacFOxBLPok9Me5dLtv+E6+snLnbzRYlJoGSO4LInQK2dMoaGi2HCzcptW7/qxrtmMg9xZHn6xZvPqfXbeG5yy2yqbm/neiJbwYy4V3IgmIPPygQNlWnUNiJRe2fjpqnmnEccWFUmsMoVlNteJgqqQUGW+O1Aq9NP5EX10FxBsZ/Mi/5CFlU7vDQV3sOqhcKqGEDOumrDVJuqNKvWeAtTMAOu1EBuZzAOnqL8741LTg3bXQrAqtjzZsHrcPlKCPo8dAjhtS/z9JvhefIgNYK3uzDq3XCBfevQEdyKy0JnXNX36G3xEi2e6ifOVXuIUlCc2WiIzaqpT7sbtZMAqxZ5BCD2RGTwqv1U0h2bpTdfRmFehkzTekeWwsOEXq0do4IBKfbo1WVmqLl0oQD4IBOsUSoetWXmagKN1WHtA+cch+WqZRkOIfawUuCq/lZYm6qbiVi1gu5nZYLz9KLX0DEacmAawUij++dhE7VuU60WPvP/rX3bXmIlsSsX/OLzAfFUq/N/c/htt+MUhCpedSQugM+Um984JdfhZHypFUxYpZykV/CYzIqUJ0CdXDU5PFBQEzUz63GG5A0T35T0uWrK7+/H1VoqWq36EWfXkQVzNrUQOOpXUczM9hWZGkE+SbZhAFYhLHf3cZJGyyxLvBf+hYyghXCSH+sAV7PxuVHSdQsj5Qlqy1H4LJfLodY8vKPWnI3PaFhVQQlnT7/vmcl0gQE8UWnxIfDPIx6lt2FWTSBR8zrF0Q5caaQ/n3Ta7VGJK8my3IAS4A3lpw9lReFGBwfn5+cHB+iGw9dQljWOAjVWUFYUk/txehir466RAP6FeFGTTOjzyFDIHkpcKwbqis9/ZPBNdC7rt+RPQP2t1f9cjNttCcUbX/gafbt8rkWtD6vPSeBfCKvWlfCDw1asSqte5I3UL2aTnkLKlTiwSjH1y+Pwcaz9iFWQZymIW+sEVuUO0g7hKoqKg9bilUfeyoFVivnzPSwb49BMXwDEYdUGE8v9+nco/r6aR2c9jnMXK2hZwty22flQVqirdp2xYJX6bxW0lLQPvlrwL3/DSFt4TAT/wtaD1+KigaGNvv/PJqlXyaPJqKEXCOaqNJuBUazimk75aPjn4DNbkMOqzQEwSVCW04SK9ep40aHBw3cfkuMTwL9wVm0BpwnxTgLH2KT4ZzrODzgrm0Ewn+gzOnAdsVJdtX2QER+sN3PwRUOIVRRbbVLpi88qzVN3EKsCC8AnZ9UOcNaktZvY/hIzdHSEazIL/jWfbJ689kfNWfgsT+GzHEZi5ZyfVctZqI1i1dCoXcmE69C+xtE4l9hXNOL8FMVKZHjkAqlwYayan5MhXpRDOxNgbh3cNB6+VsMM6OLFCuzKCKei1D64VeuL4pWSOLYf7H2hHWINBz17O+AFjuFh2iOuXtQGFeSJ3YmvEjFeyRx8sYrinkzoOfOptvtDTXJUIZJVk0lwAG3Jcr96/6un6ZHFEih331cvq8tre1btt7ZjsdP6Fw9ipsdI0VyaVbOXgqCnY9wDUVtlnqAsxd+8xHGjEIfPvK2FIKtWsFk1O09G3Ncctuqgn658w9o17DY4xnmo5Vg1JxkPdIeudzLnX6qieMatrc627mBQcMG5C0lNmFx94UxFGmajD5haC95YVs1w8ylBvT100ZButFHZgi9SUlwMLdIun9vOefBZrhJAbUWr1WbV7FayN0Elc4nzEoV7BEk+GM9CahilukDgitdwP4jPlslVgw9OqcgH6lM/W9UwO91WJlmvgupk6lcX/f58PobXZDIht715vzWIkyj2ItjypKwaObvkSTgUrw80r8UKEkQB6sH+5HN2NWAMBrDryODuDo76s1l3MXmY9g7MLY1UXkEScD1jNEHgDbUOlXbnrF8P1xKoDAWFqEDPIwV5Tys23nNvPRtxPgphqwxZltXR6KD9uo+GojNZdNCts//a640OFFNA/62sWbXueZv2CoVVnKTJ5gMyAqaGV7KnGN0yrBpxv/Kev0z27FzG55XZu54lXpLyZChQDwxJ4oN+PCmsqsAf23tM9AT2wqt7pvtage7fAwXixT5hoZPkqq0MqyRNe71mYGB8imMlVs1GOGZQOqjPe41GocBkqzwYaT2wSj+fBePuoBEhnvpfQlk1uyqXxFrMA1D/hK9Q55c5Zp4eVgmaGRhF0NWSbKpG5apZ9iJ/Mu0cWv/F3quAafZ1FcyJykENrGSAuaavFWTlVqi3BmDQn0wPZFlD1EbICdBVYVXJEjTzDeK17BWUPlfNRkPDqGQLHOne+nud6fmoVNKHxjCv66UyQkO5HGvXM4dhVSmn5yWjrMPLMIZGqVQy4FXS0Q225nxgCwnSpxnPmxZ7hFXLhaO27RxLEG61vSgebyme+SW7fvVWazZfjB967fa5OYKvTpLRHNZhkERDzEuKiWIlvHrTh3Hnv/8WZ4vFfD6foavf78/OFp/d//7DNdgEDS2MJIEiw1TvXLowVmLVaHtJoKF3SK09ULt6XIZs/1J7oIwr40Vy8HUdXc8nbbw/bIfZPXqaim1hPZ8lgg8Uk6RbrP/Cml6MR5whYB+y7SVoW7LA+/qJFBQc1JYL4DMLteV4X43fbf7r9idQhdUHzj6q0KNXOAdLfOIh7KM20tVXruNBfYzMEbkG09UQzFcKE15YJWgXX0rGgMGrTOCfQNVoX4FVK9g5YAXrVmz4A9E/vkDfwlxNJ2yBsV4M9BOjNqu1UCD4rEDwmYUuUSvHgFXy5Is1rPc0Ut3TGcMLOTH88x4z99RVc9yv9vrV7H2HbBUqth2Ky3ytIFBXzUVDkvqlrgZXHyV7oXYN0E4k/CuFwz+OglXwViFga7s8nH/xTuHMQD3S7fSd1pDdT6fVRozbvlaqHJqHrRLk18wXU9syBlt2sSk5NtE94EW3PHXVAmyVobJW2P9Qwwne7NW7pILdq7Q0q4ZxT1HwsFXQfuGfPHzpIJINvW2yigNdKbyfCLUR9s9m1QQ3e4qL+lrB9teGRJWsMbErba3GqoW6394XulOAQHbRrhe9IqsWzlZ1vm6eQjPEqA1xmhBwR/czrJ4MQjgQ0hDcU6BwT8FqNYyzr1ORADN0uAo86NH9dG8FSyd8i/uCJH5Jze4XqQhmZNh6IvIyK7JqEcuQiiZ9kYriQQ73aA4yM21VVi2SrdJK48FX7IZelAg+Q9sUy7FqFBm2FUBDCPfYrcXh6/W/V1HsYQhmdMQMl6yfDmrbolg1ktDnuF/LOwXzvtWzt3+834s+R4bwmfwGUvSTKrRhxcFsfHwhDzbOF/9WR3GEDU/qiaM0/fTGQYHFVlUEm60SaDtGm9qTi7D9vJALOExhagVRzdoi4treDtL1k82qJWOrJLncO7vORHXY/lY0qA8Gb63+bL639wmvvfm89TZIp6mE8ZnUaa+HVUv+aXXD3O/OrgaBfexMfXB1BDWajKe9kSLgzd6hvYWtaeijLOf73esk3/jBr+rVKghqrhYmUrNVUBzutGq2X6cou2Ay6UynvfNNAatifzyEvVmJ9ugPFsk+hjPTVspVK4ThnoIX91RcSBf8ZR7vrRiVbQcjRQqyYJVuNBdvCZYrRlBQ8n6SMBFVEzuErWLWVQsIioVV3GsrTkWxl6h2dxpWLelmZeIy1LhfvMKqQ8jL7RgVwZmxahLCMmwV7yl5FHYClKphr397evrxY8iAVY2Y/NQjI25TNQWrtkUQjhcN2bjHanV3PbdyuHWr4m0tldRt8lUBXMb++/Px4+7ubm1nd/emucWCVcO9qEEEDHyWuJ9umLD3JpKey3PQkKIoVsVB/KkW01T0ux8vv38htazq+9YRiGdDCREv9yIyxe2CoMv1M5RVi2OrHAVPbi5vf/z48XH78ef0HalVs/TynbGqvkTAqqhDtmDMsex6OVYN3thsVQ5/eIFmqwp4s/LusYq+kVSrxXxxoHavY1glhMKqRdg0BSQ3dtl+LslWkbpq5keyM//Vx1tUFiQSVg1DD6W0tJVz1ZYNE/6TcGHD984lgVVhpYkG8uq5aqnZKhToh4FKeGz1jn96yyiHwqqwYzdSgly1CFYtDT6jWkcviWqgVzcuR0nF61PmGIJiahzptCZi1dh11RKVYa5WTwpccvjXYHoaUV1HrlqqZUg5UZ3bjY3d+29mOrtmHQZHgXANuWoRbNWm/WYsj6c0I+rAulft+M5MDf8YeSyglzBXzd9Pm1WDuCcKDW3RsAq1qsPDBJX7ahu3zaIlfhuL36JhlVd82RHPOIUK2hgUpu4naiVeNIKtCqIOnrtMYH070LcowhLwj5HWCdokTKTrpyeVKwVbZX5LUEW7uvFnefjHGEE7Di7Nqgletgrz9RasEjywqmLexBe5QSUAOT+ssgW5sAqJzwl++Cf4C5tDJyORXLUU/USCkIJCSlbNlOOHD9XIWwX+8XJgBLk15qpFuV9F+R0b22uPN0vntFgsgTTxDeGAW0OYSMBWqU9x0KxaO34xFe/XUZLDKmkhEJ5H8il44RG0DlatwkBDaj6uWhiqnao209NzTut01sCthrfYItjTQ1g1Vj+XZdXMjxjoUtt4H8LRW+UIQE88J0dAvMsKsM8G22tl1YbRzgXNzaWP9rit4jVZGOme4u3AXDWl2fF4WabHyza590jnslP9/tNkCvJ6vGycxwPgHL943XOU6srwH84K6acH/mUdVo0gnC0HDdGwCqKinKpGzs7qzvOHquJHbIzkgVWuoFhYNcyAfgmitq3ilFIQTHSPoLB+MuDfVgJWTeHu/N/w9UzNw9NvpuL5BujysErLoE9Z4QNftILeejLrZdUE89t96LqhWnt8v8N1b5lHe9LDKhkzaJgtp05stuQVT4Ay2Cob9zSFkzBghsr0P2HDg39LWHxakA2rhDSwCn2i7IigNrcgqLV9FtnPSPgXDqsU5Q/b+Ko7tePfmGcJ+wbokrAK7QQjHJSTOo6Cg7WcAGW4322TVQIMf9Dp14tuKsp6PhXtDRN2bq975hYs1nMCNAirbh8D6qEvfzz//skRNBT77bPUsAqn96LvWkF/4yioRohPwqpVKhjvFKx7voIQTlO9Pfa5zmpt9/H+5mez2UR/StBQJe8+UnAF0a3uLyve1orb6gjCweGqgVoNi7kAc91+hNHPMEFUK5tV83y8HjHzG8/vL0MVzssKt44PDYeAbWx4QMKCLDeKPxe/nhOgtr0o6gtWD2007OzUqsff/zx9wzt8f/sEqISzl8E5tmuyFwNm+qp27V/wKjfV3RqMAYfP30//fDxJKBI0s8xC4lnm5/mWh1Van4QFPIKEPhRHuVXhH8Y9WwRWbSGEozpfRIe3EsQ9WxYaspDYlo2G8K7nlhefYUEl9xG7ddsRj1rLtCDSigQRMgY86LDVIKM5H9riS/5+2oIqXkH+fhIvugSsErzffGHhs7SwihRsR7uBuaw1XYWV4R/HLQmrmEkI2VUKa5RJyX1KQbDQVoZ/WEEXVlG4JwCrJJv2KhE0VOG8ZFgAn6WEVcbMUXBbkNCCaSCHwb+ofi7NqvXGmpTgG6DJnAwDVll8KOhISBAEo2KbKejvsWrjwSs+MvWXwoS1OYjOuJTR17nBpxYU9FdZNa4jXk05/9cK/N8AXRpWndn13aw4ONDWAf84Cv64N8aP6GY8iOJg0TQqEX/rRW1MQTS6clttHkZEvFylcSGeRwiK7if9S47xkiJg1YOYAeB6igd+yVy1ofTKglWScygT27WcwbkjK8O/1EkIPZK8299XcM2DpMsl1ANNls3eon+0UFj2Il/YC3gsSMGF49ZUVy0NrDIUkpIExMHew4iTNSnKdfI4dVSW5VFvfNa/AqJ49TCUWB5PsheAoItfPK+tB/5tclsE2iBYVfLDqhJCQyUvrCqV7OKVAIiZVnfcM4fDBlcihahKqPqRBG+N4XCoq73e66Tbv6gDq+zDvD0su7CqVHbFl+xEJ7FXdsGWF/6l6icRXywtk6tG743gJObBUWu21+1OFujqdhezWat1NHDUsv7waMzpYaiDdyrRD9YL/5bKVZPMI/8OHqsiB/1rcdA999vLiN7Wtb8lAD6D8C+7PPyLY9XCYJWc5swdAPV5W5Z8sKpxdkAdVXBcqNhjwL8gabcsq5YYVpWkz2QnA4D4ttfWtCCsmgKZcjLOXsSVvFb4t3yuGq/xsSqiclDjA04XGLCqJy6oj1U522VgX1pznSis4HK5arq6CD2Qhszw6JPUumLBqp4Il3o2rMq7u2UDeb3wL8iqReMeb2teb/Q+6/7ynMivDq4nr5WGEYbljB4AC8P5ZdN5VnyIQ4Gp+xmTq8az2Sr6JR1M5hcZUuBIFDNH/e7klcOl2MJh1VjMDBru23Z98luDW+6oQkQ/lz/aY6c0S2jh5NUAAAMUSURBVJLW4PBnehBBxS5zSNlLCdUVA+cVR5Cb+CO2/wJbHrbgjWWrAqwan8Tj8droDS5l9yXH440dAwQz2XNUIdF+R1pWreTgnooXDVGwKkfQUMVGQ7kSA1YRQX5YVSqhfElxUbJhlf7qbscPSiVKPFtQ6n4SL/qvWDWjd4T067qCqE9coJxC9wvp2TVtqjIVXIFVi4JVkoDjnYg/SEAEUfqJE45WkBUHl+knVypB3LMFcQ/E3VsQ4ZQgGtragrcK/BHDKtKKLbYE0dAWYau2hApq3YIAirTC2za85YmgIhGEWol4uB6cYHwndoa2IJ0ev/7QFh8tKGU/lzoBugSrJmkTckAJTURbPPXZQ3AU+AR8MifzF0+ApmHVDFu9N1N3BNGpFAM17Ym2NbNq4YE+DlbB/+vAroYhziVX/JhKZ6qr8WV1l+xnKE0Vgs8CrdGwqmJUpi0LsYJM23B+2/h09QODZj49PkvWT47xktZ2ApSX5N5Z3VYEDp/hvm2q/h6A85M9K76AVUtzAnTY7rrLDfDWll1BB9SRSPwFgb9WVpdjOqoEbFWUx8tKmjHyVAcHmTFys9Z285BOWhbnDS4U/q2JVQuBVTYaKnlYNT8+w7CqZMGqEmcMh1JvMvN85ACIe5KBBGFYVcpRH5UBYMrR8C8gPgH8i+ynP0wscQIUPoJS0OEqotybjveu/YUOAJiNDBdWcT16erbUtPAvbT9jWLVECkoLa6AYNRxAZm9E2YukUYW+QGZ/yK0G/+L7ueWgoS0XDdm4Bw6yjXtypVLORkNwQnhhlT5ifz8FgKsOpoNt8cP9OmWXXVQp3xG/nRD+petnEicTdQTA9gIyv7jykBe4au/E5GhYRRdCB6DLc6vBv39xAtQznUbjz6O6/Vna2WJalCW6ip2kde03AMS3CbTZ1eDfPzgB6odVuiZr23DWojCBX7EHVnWs2QnE+lmPM5LBv0gckZRVi9xcLATRULA1fluyMR2QnYrM9eLc0PMR4iMFpe5nkFVbFmxHwqrpVf3qejafvJ7LpdC3na4ASMJ+/g8sQzWjp/7HvAAAAABJRU5ErkJggg=="
            class="h-5 w-5 rounded-full"
            alt=""
          />
          <div class="flex flex-col">
            <p class="text-sm font-bold">Python</p>
            <a href="https://www.python.org" class="text-xs">www.Python.org</a>
          </div>
        </div>
        <div class="text-left">
          <a href="#" class="text-blue-500 text-xl">Python Openings</a>
          <p class="flex-wrap">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
            explicabo rerum atque nostrum! Vel corrupti, esse iusto voluptate
            sapiente odit.
          </p>
        </div>
      </div>

      <div class="flex justify-center gap-x-2 bottom-0 absolute">
        <a href="" class="text-blue-500">1</a>
        <a href="" class="text-blue-500">2</a>
        <a href="" class="text-blue-500">3</a>
        <a href="" class="text-blue-500">4</a>
        <a href="" class="text-blue-500">Next</a>
      </div>
    </div>
  </div>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
export default {
  name: "ListView",
  components: {
    TopBar,
  },
};
</script>

<style></style>
