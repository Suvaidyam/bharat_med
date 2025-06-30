<template>
	<div class="p-6">
		<!-- Header -->
		<div class="flex items-center space-x-2 mb-6">
			<button class="text-gray-500 hover:text-black">
				<span class="text-xl">&larr;</span>
			</button>
			<h1 class="text-2xl font-semibold">New Room Allotment</h1>
		</div>

		<!-- Form Card -->
		<div class="bg-white shadow rounded-lg p-6">
			<h2 class="text-lg font-semibold mb-2">Room Allotment Details</h2>
			<p class="text-sm text-gray-500 mb-6">
				Assign a room to a patient. Fill in all the required information below.
			</p>

			<!-- Grid Layout -->
			<div class="grid md:grid-cols-2 gap-6">
				<!-- Left Column -->
				<div class="space-y-4">
					<h3 class="text-sm font-medium text-gray-700">Patient Information</h3>
					<div>
						<label class="block text-sm font-medium">Patient ID</label>
						<input type="text" placeholder="Enter patient ID" class="input" />
					</div>
					<div>
						<label class="block text-sm font-medium">Patient Name</label>
						<input type="text" placeholder="Enter patient name" class="input" />
					</div>
					<div>
						<label class="block text-sm font-medium">Attending Doctor</label>
						<select class="input">
							<option>Select doctor</option>
						</select>
					</div>
					<div>
						<label class="block text-sm font-medium">Emergency Contact</label>
						<input type="text" placeholder="Enter emergency contact" class="input" />
					</div>

					<h3 class="text-sm font-medium text-gray-700 mt-6">Allotment Details</h3>
					<div>
						<label class="block text-sm font-medium">Allotment Date</label>
						<input type="date" class="input" />
					</div>
					<div>
						<label class="block text-sm font-medium">Expected Discharge Date</label>
						<input type="date" class="input" />
					</div>
					<div>
						<label class="block text-sm font-medium">Purpose of Admission</label>
						<textarea
							rows="2"
							placeholder="Enter purpose of admission"
							class="input"
						></textarea>
					</div>
				</div>

				<!-- Right Column -->
				<div class="space-y-4">
					<h3 class="text-sm font-medium text-gray-700">Room Information</h3>
					<div>
						<label class="block text-sm font-medium">Room Number</label>
						<select class="input">
							<option>Select room number</option>
						</select>
					</div>
					<div>
						<label class="block text-sm font-medium">Room Type</label>
						<select class="input">
							<option>Select room type</option>
						</select>
					</div>
					<div>
						<label class="block text-sm font-medium">Department</label>
						<select class="input">
							<option>Select department</option>
						</select>
					</div>
					<div>
						<label class="block text-sm font-medium">Special Requirements</label>
						<textarea
							rows="2"
							placeholder="Enter any special requirements"
							class="input"
						></textarea>
					</div>

					<h3 class="text-sm font-medium text-gray-700 mt-6">Billing Information</h3>
					<div>
						<label class="block text-sm font-medium">Payment Method</label>
						<select class="input">
							<option>Select payment method</option>
						</select>
					</div>
					<div>
						<label class="block text-sm font-medium"
							>Insurance Details (if applicable)</label
						>
						<textarea
							rows="2"
							placeholder="Enter insurance details"
							class="input"
						></textarea>
					</div>
					<div>
						<label class="block text-sm font-medium">Additional Notes</label>
						<textarea
							rows="2"
							placeholder="Enter any additional notes"
							class="input"
						></textarea>
					</div>
				</div>
			</div>

			<!-- Buttons -->
			<div class="flex justify-end mt-8 space-x-3">
				<button class="px-4 py-2 bg-gray-100 rounded hover:bg-gray-200">Cancel</button>
				<button class="px-4 py-2 bg-black text-white rounded hover:bg-gray-800">
					Create Allotment
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
// no reactive data yet
</script>
