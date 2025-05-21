<template>
	<section
		class="min-h-screen flex flex-col md:flex-row items-center justify-center bg-white px-4 py-10"
	>
		<!-- Left Side Image -->
		<div class="w-full md:w-1/2 flex justify-center mb-10 md:mb-0">
			<img
				src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGRvY3RvcnxlbnwwfHwwfHx8MA%3D%3D"
				alt="Doctor"
				class="max-w-sm md:max-w-md lg:max-w-lg"
			/>
		</div>

		<!-- Right Side Form -->
		<div class="w-full md:w-1/2 max-w-md mx-auto">
			<h2 class="text-2xl md:text-3xl font-bold text-gray-800 mb-2">Get Started</h2>
			<p class="text-sm text-gray-600 mb-6">Register Your Virtual Clinic</p>

			<form class="space-y-4">
				<input
					type="text"
					placeholder="First Name*"
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
				<input
					type="text"
					placeholder="Last name*"
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
				<select
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				>
					<option disabled selected>Educational Qualification</option>
					<option>MBBS</option>
					<option>MD</option>
					<option>DO</option>
				</select>
				<select
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				>
					<option disabled selected>Specialization</option>
					<option>Cardiology</option>
					<option>Neurology</option>
					<option>General Physician</option>
				</select>
				<input
					type="email"
					placeholder="Email*"
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
				<input
					type="text"
					placeholder="Pin Code*"
					class="w-full px-4 py-2 bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>

				<button
					type="submit"
					class="w-full bg-cyan-500 hover:bg-cyan-600 text-white py-2 rounded-full font-semibold transition duration-200"
				>
					Submit
				</button>
			</form>
		</div>
	</section>
</template>
