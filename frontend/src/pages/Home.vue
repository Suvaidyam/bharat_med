<template>
	<div>
		<Navbar />
		<div>
			<img
				class="h-[336px] w-full object-cover"
				src="https://images.unsplash.com/photo-1726390415318-e6872be3da8a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
				alt=""
			/>
		</div>
		<div>
			<section class="px-4 py-10 md:py-16 bg-white">
				<div class="flex flex-col md:flex-row items-center gap-8 md:gap-12">
					<!-- Text Content -->
					<div class="w-full md:w-1/2">
						<h2 class="text-2xl md:text-3xl font-semibold text-gray-900 mb-4">
							About Connect2Clinic
						</h2>
						<p class="text-gray-700 mb-4">
							Connect2Clinic, an exceptional digital initiative pioneered by Alkem
							Labs, is dedicated to transforming the management of healthcare
							practices. As a subsidiary of Alkem Labs, our unwavering goal is to
							carry forward the company’s rich tradition of excellence and unwavering
							dedication to healthcare.
						</p>
						<p class="text-gray-700">
							This cutting-edge platform is an AI-driven, comprehensive solution that
							not only streamlines and elevates the patient experience but also
							empowers healthcare providers with state-of-the-art tools and
							technologies.
						</p>
					</div>

					<!-- Image -->
					<div class="w-full md:w-1/2 flex justify-center">
						<img
							src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8ZG9jdG9yfGVufDB8fDB8fHww"
							alt="Connect2Clinic Building"
							class="max-w-full h-auto"
						/>
					</div>
				</div>
			</section>
		</div>
		<section class="bg-[#FBE6C1] py-10 px-4">
			<div class="flex flex-col md:flex-row items-center gap-8">
				<!-- Left Side: Image -->
				<div class="w-full md:w-1/2 flex justify-center">
					<img
						src="https://www.connect2clinic.com/static/media/Mask%20Group%20116.2fa2d021.png"
						alt="Doctor"
						class="max-w-xs md:max-w-sm lg:max-w-md"
					/>
				</div>

				<!-- Right Side: Features -->
				<div class="w-full md:w-1/2">
					<h2 class="text-xl md:text-2xl font-semibold text-gray-900 mb-6">
						Explore our Features
					</h2>

					<!-- Feature Card -->
					<div
						v-for="(feature, index) in features"
						:key="index"
						class="bg-white p-5 mb-4 flex items-start gap-4 shadow-sm"
					>
						<div class="text-blue-600 text-2xl">
							<component :is="feature.icon" class="w-6 h-6" />
						</div>
						<div>
							<h3 class="font-semibold text-gray-800 mb-1">{{ feature.title }}</h3>
							<p class="text-gray-600 text-sm">
								{{ feature.description }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</section>
		<footer class="bg-black text-white text-sm px-4 py-10 md:py-14">
			<div class="">
				<!-- Top Grid -->
				<div class="grid grid-cols-1 md:grid-cols-4 gap-8 border-b border-gray-700 pb-8">
					<!-- Address -->
					<div>
						<h3 class="font-bold mb-2">ADDRESS</h3>
						<p>
							3rd Floor, Alkem House, Marathon Innova<br />
							Corporate Building, Senapati Bapat Marg,<br />
							Lower Parel, Mumbai, Maharashtra - 400013.
						</p>
					</div>

					<!-- Company Links -->
					<div>
						<h3 class="font-bold mb-2">COMPANY</h3>
						<ul class="space-y-1">
							<li><a href="#" class="hover:underline">About Us</a></li>
							<li><a href="#" class="hover:underline">Our Features</a></li>
							<li><a href="#" class="hover:underline">FAQ'S</a></li>
							<li><a href="#" class="hover:underline">Terms</a></li>
							<li><a href="#" class="hover:underline">Privacy</a></li>
						</ul>
					</div>

					<!-- Contact -->
					<div>
						<h3 class="font-bold mb-2">CONTACT</h3>
						<div class="flex items-center space-x-2">
							<span>📞</span>
							<span>1800 267 9899</span>
						</div>
						<div class="flex items-center space-x-2 mt-2">
							<span>✉️</span>
							<span>hello@connect2clinic.com</span>
						</div>
					</div>

					<!-- App Download -->
					<div>
						<h3 class="font-bold mb-2">DOWNLOAD THE CONNECT2CLINIC APP</h3>
						<div class="flex space-x-2">
							<!-- <img src="@/assets/appstore.png" alt="App Store" class="h-10" />
							<img src="@/assets/googleplay.png" alt="Google Play" class="h-10" /> -->
						</div>
					</div>
				</div>

				<!-- Social Links -->
				<div class="mt-6 flex justify-center md:justify-end space-x-4 text-xl">
					<h3 class="font-bold mr-2 text-sm">FOLLOW US ON</h3>
					<a href="#" class="hover:text-gray-400">🌐</a>
					<a href="#" class="hover:text-gray-400">🐦</a>
					<a href="#" class="hover:text-gray-400">🔗</a>
					<a href="#" class="hover:text-gray-400">▶️</a>
				</div>
			</div>
		</footer>
		<!-- <Register /> -->
		<!-- <FAQs /> -->
	</div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'

import { MessageCircle, PlusSquare, Shield } from 'lucide-vue-next'
// import FAQs from './FAQs.vue'
// import Register from './Register.vue'

const features = [
	{
		icon: MessageCircle,
		title: 'Booking via WhatsApp',
		description:
			'Receive real-time appointment bookings, as patients can easily scan unique QR code and schedule appointments with their doctors in real time.',
	},
	{
		icon: PlusSquare,
		title: 'Queue Management System',
		description:
			'Manage patient queues, reduce wait times, and enhance overall patient experience with our innovative QMS.',
	},
	{
		icon: Shield,
		title: 'Smart eRx',
		description:
			'With multi-lingual smart eRx feature, easily generate electronic prescriptions and share with patients directly, eliminating the need for paper prescriptions.',
	},
]
</script>
