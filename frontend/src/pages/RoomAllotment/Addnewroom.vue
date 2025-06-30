<template>
	<div class="p-4">
		<div class="flex items-center space-x-2 mb-6">
			<button class="text-xl font-bold">&larr;</button>
			<h1 class="text-2xl font-semibold">Add New Room</h1>
		</div>

		<div class="bg-white shadow rounded-lg p-6">
			<h2 class="text-lg font-semibold mb-1">Room Details</h2>
			<p class="text-sm text-gray-500 mb-6">
				Add a new room to the hospital inventory. Fill in all the required information
				below.
			</p>

			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<!-- Basic Information -->
				<div>
					<h3 class="font-medium mb-4">Basic Information</h3>

					<div class="space-y-4">
						<div>
							<label class="block text-sm font-medium">Room Number</label>
							<input
								type="text"
								placeholder="Enter room number"
								class="mt-1 w-full border rounded px-3 py-2"
							/>
							<p class="text-xs text-gray-400 mt-1">Enter a unique room number</p>
						</div>

						<div>
							<label class="block text-sm font-medium">Room Type</label>
							<select class="mt-1 w-full border rounded px-3 py-2">
								<option>Select room type</option>
							</select>
						</div>

						<div>
							<label class="block text-sm font-medium">Department</label>
							<select class="mt-1 w-full border rounded px-3 py-2">
								<option>Select department</option>
							</select>
						</div>

						<div>
							<label class="block text-sm font-medium">Floor</label>
							<select class="mt-1 w-full border rounded px-3 py-2">
								<option>Select floor</option>
							</select>
						</div>
					</div>
				</div>

				<!-- Additional Details -->
				<div>
					<h3 class="font-medium mb-4">Additional Details</h3>

					<div class="space-y-4">
						<div>
							<label class="block text-sm font-medium">Capacity (Beds)</label>
							<select class="mt-1 w-full border rounded px-3 py-2">
								<option>Select capacity</option>
							</select>
						</div>

						<div>
							<label class="block text-sm font-medium">Price Per Day</label>
							<input
								type="text"
								placeholder="Enter price"
								class="mt-1 w-full border rounded px-3 py-2"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium">Status</label>
							<select class="mt-1 w-full border rounded px-3 py-2">
								<option>Available</option>
								<option>Unavailable</option>
							</select>
						</div>

						<div>
							<label class="block text-sm font-medium">Description</label>
							<textarea
								rows="3"
								placeholder="Enter room description"
								class="mt-1 w-full border rounded px-3 py-2"
							></textarea>
						</div>
					</div>
				</div>
			</div>

			<!-- Facilities -->
			<div class="mt-8">
				<h3 class="font-medium mb-4">Facilities</h3>
				<div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
					<label><input type="checkbox" class="mr-2" /> Television</label>
					<label><input type="checkbox" class="mr-2" /> Air Conditioning</label>
					<label><input type="checkbox" class="mr-2" /> WiFi</label>
					<label><input type="checkbox" class="mr-2" /> Telephone</label>
					<label><input type="checkbox" class="mr-2" /> Attached Bathroom</label>
					<label><input type="checkbox" class="mr-2" /> Wheelchair Accessible</label>
					<label><input type="checkbox" class="mr-2" /> Oxygen Supply</label>
					<label><input type="checkbox" class="mr-2" /> Nurse Call Button</label>
				</div>
			</div>

			<!-- Additional Notes -->
			<div class="mt-6">
				<label class="block text-sm font-medium mb-1">Additional Notes</label>
				<textarea
					rows="3"
					class="w-full border rounded px-3 py-2"
					placeholder="Enter any additional notes"
				></textarea>
			</div>

			<!-- Buttons -->
			<div class="mt-6 flex justify-end space-x-4">
				<button class="px-4 py-2 border rounded hover:bg-gray-100">Cancel</button>
				<button class="px-4 py-2 bg-black text-white rounded hover:bg-gray-800">
					Add Room
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
// You can add reactive state, emits, or form handling here using Vue's Composition API if needed
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
