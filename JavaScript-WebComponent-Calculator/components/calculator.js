(function() {
    let template = `<style>
            table {
                border: 1px solid #777;
                padding: 5px;
            }
            tr {
                margin-top: 5px;
                background: #f2f2f2;
            }
            tr:first-child {
                background: cornflowerblue;
                color: #fff;
            }
            tr:nth-child(even) {
                background: #fff;
            }
            td > div {
                width: 120px;
            }
            td > input, td > select, td > button {
                width: 200px;
            }
            tr .header {
                text-align: center;
                font-size: 120%;
                font-weight: bold;
                width: 100%;
            }
            tr .message {
                width: 100%;
                color: blue;
                text-align: center;
                display: none;
            }
        </style>
        <table class="calcForm" cellspacing=0>
            <tr>
                <td colspan="4"><div class="header"></div></td>
            </tr>
            <tr>
                <td><div class="firstNumber"></div></td>
                <td><input type="number" class="inputFirstNumber"></td>
                <td><div class="secondNumber"></div></td>
                <td><input type="number" class="inputSecondNumber"></td>
            </tr>
            <tr>
                <td><div class="selectOperation"></div></td>
                <td><select class="inputOperation">
                <option value="select">Select Operation</option>
                    <option value="add">Addition</option>
                    <option value="sub">Subtraction</option>
                    <option value="mul">Multiplication</option>
                    <option value="div">Division</option></select>
                </td>
                <td><div class="result"></div></td>
                <td><input type="text" class="output"></td>
            </tr>
            <tr>
                <td><div class="message"></div></td>
            </tr>
        </table>`;

        class Calculator extends HTMLElement {

        // Fires when an instance of the element is created.
        connectedCallback() {
           
            this.attachShadow({mode: 'open'}).innerHTML = template;
            console.log('jjvvvvvjj');
            //Grab the elements from the shadow root
            this.$header = this.shadowRoot.querySelector('.header');
            this.$message = this.shadowRoot.querySelector('.message');
            this.$firstNumber = this.shadowRoot.querySelector('.firstNumber');
            this.$secondNumber = this.shadowRoot.querySelector('.secondNumber');
            this.$selectOperation = this.shadowRoot.querySelector('.selectOperation');
            this.$result = this.shadowRoot.querySelector('.result');

            this.$inputFirstNumber = this.shadowRoot.querySelector('.inputFirstNumber');
            this.$inputSecondNumber = this.shadowRoot.querySelector('.inputSecondNumber');
            this.$inputOperation = this.shadowRoot.querySelector('.inputOperation');
            this.$output = this.shadowRoot.querySelector('.output');
            this.$output.value = 0;

            //Call the draw function initially
            this.draw();

            //Call the fetchaddressdata function to fetech the data
            this.$inputOperation.addEventListener("click", this.fetchAddressData.bind(this));
        }

        fetchAddressData() {
            console.log('jjjj');
            this.$message.style.display = "block";
            console.log(this.$inputOperation);
            let firstNumValue = this.$inputFirstNumber.value;
            let secondNumValue = this.$inputSecondNumber.value;
            let operation = this.$inputOperation.value;
            if (operation == "add") {
                this.$output.value = parseFloat(firstNumValue) + parseFloat(secondNumValue);
            } else if (operation == "sub"){
                this.$output.value = parseFloat(firstNumValue) - parseFloat(secondNumValue);
            } else if (operation == "mul"){
                this.$output.value = parseFloat(firstNumValue) * parseFloat(secondNumValue);
            }  else if (operation == "div"){
                this.$output.value = parseFloat(firstNumValue) / parseFloat(secondNumValue);
            } else {
                    this.$output.value = "Please Select The valid Operation";
            }
            this.$message.style.display = "none";
        }

      
        draw() {
            this.$header.innerHTML = "Reusable Calculator Component";
            this.$firstNumber.innerHTML = "First Number";
            this.$secondNumber.innerHTML = "Second Number";
            this.$selectOperation.innerHTML = "Select Operation";
            this.$result.innerHTML = "Result";
            this.$message.innerHTML = "Please Wait...";
        }
    }
    customElements.define('wc-calculator', Calculator);
})();