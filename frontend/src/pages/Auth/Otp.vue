<template>
	<div
		class="pt-[62px] flex flex-col items-center min-h-screen bg-secondary"
		style="background: #f5f5f5"
	>
		<!-- Main Content Centered -->
		<main
			class="flex flex-col items-center text-center w-full px-4 min-h-[calc(100vh-64px)] justify-center"
		>
			<!-- OTP Verification Box -->
			<div class="bg-white p-6 mt-[36px] rounded-sm w-[443px] max-w-full">
				<h2 class="text-[20px] font-medium font-poppins text-gray-900 text-center">
					OTP Verification
				</h2>
				<p class="text-gray-600 text-center mt-1 text-[12px] font-normal">
					We've shared a 6-digit OTP on
					<span class="text-[#001f3f] font-semibold">{{
						email || 'sample@gmail.com'
					}}</span>
				</p>

				<!-- OTP Input -->
				<div class="flex justify-center space-x-2 mt-4">
					<div style="display: flex; flex-direction: row">
						<v-otp-input
							ref="otpInput"
							input-classes="otp-input"
							:conditionalClass="['one', 'two', 'three', 'four', 'five', 'six']"
							separator="-"
							:num-inputs="6"
							v-model="bindValue"
							:should-auto-focus="true"
							:should-focus-order="true"
							@on-change="handleOnChange"
							@keyup.enter="verifyOTP"
							input-type="number"
							@on-complete="handleOnComplete"
							:placeholder="['*', '*', '*', '*', '*', '*']"
						/>
					</div>
				</div>

				<!-- Verify Button -->
				<router-link to="/mykarma">
					<button
						@click.prevent="verifyOTP"
						class="w-full flex items-center justify-center h-10 bg-[#001f3f] text-white py-2 text-[12px] mt-6 rounded-sm hover:bg-[#0f375f]"
					>
						<div class="h-5 w-5" v-if="loading">
							<div
								class="animate-spin h-full w-full rounded-full border-[2px] flex justify-center items-center border-dotted border-[#fff]"
							>
								<div
									class="w-3 h-3 rounded-full border-dashed border-[1px] border-[#fff]"
								></div>
							</div>
						</div>
						<p v-else>VERIFY</p>
					</button>
				</router-link>

				<!-- Resend OTP -->
				<p class="text-center text-[14px] text-gray-600 mt-4">
					Didn't receive?
					<a
						href="#"
						@click.prevent="resendOTP"
						class="text-[#001f3f] font-normal text-[14px]"
						>Resend OTP</a
					>
				</p>
			</div>
		</main>
	</div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

//   const call = inject('call')
const router = useRouter()
const route = useRoute()
const loading = ref(false)
const email = ref(route.query.email || '')
const bindValue = ref('') // Fix for OTP binding

const getOTP = async () => {
	if (!email.value) {
		toast.error('Please enter an email')
		return
	}

	try {
		const response = await fetch(
			'http://hosp.localhost:8000/api/method/bharat_med.controllers.email.send_otp',
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					email: email.value,
				}),
			},
		)
		if (response.status === 200) {
			toast.success('OTP sent successfully', {
				position: 'top-right',
				autoClose: 5000,
				hideProgressBar: false,
				closeOnClick: true,
				pauseOnHover: true,
			})
		} else {
			toast.error('Failed to send OTP', {
				position: 'top-right',
				autoClose: 5000,
				hideProgressBar: false,
				closeOnClick: true,
				pauseOnHover: true,
			})
		}
	} catch (error) {
		toast.error('Failed to send OTP', {
			position: 'top-right',
			autoClose: 5000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
		})
	}
}

const verifyOTP = async () => {
	if (bindValue.value.length !== 6) {
		toast.error('Please enter a 6-digit OTP', {
			position: 'top-right',
			autoClose: 5000,
			hideProgressBar: false,
			closeOnClick: true,
			pauseOnHover: true,
		})
		return
	}
	if (!email.value) {
		router.push('/login')
		return
	}
	if (route.query.full_name) {
		const response = await fetch(
			'http://hosp.localhost:8000/api/method/bharat_med.controllers.email.register_verify_otp',
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					email: email.value,
					otp: bindValue.value,
					full_name: route.query.full_name,
				}),
			},
		)
		if (response.status === 200) {
			toast.success('OTP verified successfully')
			router.push('/dashboard')
			window.location.reload()
		} else {
			toast.error(response.message)
		}
	} else {
		try {
			loading.value = true
			const response = await fetch(
				'http://hosp.localhost:8000/api/method/bharat_med.controllers.email.verify_otp',
				{
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify({
						email: email.value,
						otp: bindValue.value,
					}),
				},
			)
			loading.value = false

			if (response.status === 200) {
				toast.success('OTP verified successfully', {
					position: 'top-right',
					autoClose: 2000,
					hideProgressBar: false,
					closeOnClick: true,
					pauseOnHover: true,
				})
				router.push('/dashboard')

				setTimeout(() => {
					window.location.reload()
				}, 2000)
			} else {
				toast.error('Invalid OTP, please try again', {
					position: 'top-right',
					autoClose: 2000,
					hideProgressBar: false,
					closeOnClick: true,
					pauseOnHover: true,
				})
			}
		} catch (error) {
			loading.value = false

			toast.error('Failed to verify OTP', {
				position: 'top-right',
				autoClose: 2000,
				hideProgressBar: false,
				closeOnClick: true,
				pauseOnHover: true,
			})
		}
	}
}

const resendOTP = () => {
	getOTP()
}

// Add this function to handle OTP completion
const handleOnComplete = (value) => {
	// Automatically verify when all digits are entered
	verifyOTP()
}

// Add this function to handle OTP changes
const handleOnChange = (value) => {
	bindValue.value = value
}
</script>

<style>
.otp-input {
	width: 40px;
	min-width: 40px !important;
	height: 40px;
	padding: 5px;
	margin: 0 10px;
	font-size: 20px;
	border-radius: 4px;
	border: 1px solid rgba(0, 0, 0, 0.3);
	text-align: center;
}

.otp-input:focus {
	border-color: #d45a08;
}

/* Background colour of an input field with value */
.otp-input.is-complete {
	background-color: #e4e4e4;
}

.otp-input::-webkit-inner-spin-button,
.otp-input::-webkit-outer-spin-button {
	-webkit-appearance: none;
	margin: 0;
}

input::placeholder {
	font-size: 15px;
	font-weight: 600;
}
</style>
