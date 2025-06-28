<template>
	<div class="p-6">
		<!-- Header -->
		<div class="flex justify-between items-center mb-2">
			<h1 class="text-2xl font-semibold">Suppliers</h1>
			<div class="flex gap-2">
				<button class="px-4 py-2 text-sm bg-black text-white rounded hover:bg-gray-800">
					+ Add Supplier
				</button>
				<button
					class="flex items-center gap-1 px-4 py-2 text-sm bg-gray-100 rounded hover:bg-gray-200"
				>
					<span class="material-icons text-base">download</span> Export
				</button>
			</div>
		</div>
		<p class="text-sm text-gray-500 mb-6">Manage your inventory suppliers and vendors</p>

		<!-- Stat Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 mb-6">
			<div class="p-4 bg-white border rounded shadow-sm">
				<div class="flex justify-between items-center mb-2">
					<p class="text-sm text-gray-600 font-medium">Total Suppliers</p>
					<span class="material-icons text-gray-400 text-sm">local_shipping</span>
				</div>
				<p class="text-lg font-semibold text-gray-800">38</p>
				<p class="text-xs text-green-500">+3 new this quarter</p>
			</div>
			<div class="p-4 bg-white border rounded shadow-sm">
				<div class="flex justify-between items-center mb-2">
					<p class="text-sm text-gray-600 font-medium">Active Orders</p>
					<span class="material-icons text-gray-400 text-sm">local_shipping</span>
				</div>
				<p class="text-lg font-semibold text-gray-800">12</p>
				<p class="text-xs text-green-500">+4 arriving this week</p>
			</div>
			<!-- <StatCard
				title="Total Suppliers"
				value="38"
				subtitle="+3 new this quarter"
				icon="event_note"
			/>
			<StatCard
				title="Active Orders"
				value="12"
				subtitle="4 arriving this week"
				icon="inventory_2"
			/> -->
			<div class="p-4 bg-white border rounded shadow-sm">
				<div class="flex justify-between items-center mb-2">
					<p class="text-sm text-gray-600 font-medium">Top Supplier</p>
					<span class="material-icons text-yellow-500 text-sm">star</span>
				</div>
				<p class="text-lg font-semibold text-gray-800">MedPlus</p>
				<p class="text-xs text-gray-500">98% reliability rating</p>
			</div>
			<div class="p-4 bg-white border rounded shadow-sm">
				<div class="flex justify-between items-center mb-2">
					<p class="text-sm text-gray-600 font-medium">Monthly Spend</p>
					<span class="material-icons text-gray-400 text-sm">local_shipping</span>
				</div>
				<p class="text-lg font-semibold text-gray-800">$24,350</p>
				<p class="text-xs text-red-500">-8% from last month</p>
			</div>
		</div>

		<!-- Filters -->
		<div class="flex flex-wrap gap-4 items-center mb-4">
			<input
				type="text"
				placeholder="Search suppliers..."
				class="border px-3 py-2 rounded w-full sm:w-60"
			/>
			<select class="border px-3 py-2 rounded">
				<option>All Categories</option>
				<option>Medical Supplies</option>
				<option>Medications</option>
				<option>Office Supplies</option>
			</select>
			<select class="border px-3 py-2 rounded">
				<option>Active</option>
				<option>Inactive</option>
			</select>
		</div>

		<!-- Filter Tabs -->
		<div class="flex gap-2 text-sm mb-4">
			<button class="px-3 py-1 bg-gray-900 text-white rounded">All Suppliers</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				Preferred
			</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				Medications
			</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				Medical Supplies
			</button>
		</div>

		<!-- Supplier Table -->
		<div class="bg-white border rounded shadow-sm">
			<div class="p-4 border-b">
				<h3 class="font-semibold text-gray-800">Supplier Directory</h3>
				<p class="text-sm text-gray-500">
					A comprehensive list of all your suppliers and vendors
				</p>
			</div>
			<div class="overflow-auto">
				<table class="min-w-full text-sm text-left">
					<thead class="bg-gray-100 text-gray-600 uppercase">
						<tr>
							<th class="px-4 py-2">ID</th>
							<th class="px-4 py-2">Name</th>
							<th class="px-4 py-2">Category</th>
							<th class="px-4 py-2">Contact</th>
							<th class="px-4 py-2">Rating</th>
							<th class="px-4 py-2">Status</th>
							<th class="px-4 py-2">Actions</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="s in suppliers" :key="s.id" class="border-b hover:bg-gray-50">
							<td class="px-4 py-2 font-medium">{{ s.id }}</td>
							<td class="px-4 py-2">{{ s.name }}</td>
							<td class="px-4 py-2">{{ s.category }}</td>
							<td class="px-4 py-2">
								<span class="flex items-center gap-1">
									<span class="material-icons text-sm text-gray-500">email</span>
									{{ s.contact }}
								</span>
							</td>
							<td class="px-4 py-2">
								<span v-html="renderStars(s.rating)"></span>
							</td>
							<td class="px-4 py-2">
								<span
									class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded-full"
									>Active</span
								>
							</td>
							<td class="px-4 py-2">
								<span class="material-icons text-gray-500 cursor-pointer"
									>more_vert</span
								>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-4">
			<!-- Featured Suppliers -->
			<div class="lg:col-span-2">
				<div class="bg-white p-4 rounded border shadow-sm">
					<h2 class="text-lg font-semibold mb-1">Featured Suppliers</h2>
					<p class="text-sm text-gray-500 mb-4">
						Your top-rated and most reliable suppliers
					</p>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
						<div
							v-for="supplier in featuredSuppliers"
							:key="supplier.name"
							class="border rounded p-4 flex flex-col justify-between"
						>
							<div>
								<div class="flex justify-between items-start mb-1">
									<h3 class="font-semibold text-gray-800">
										{{ supplier.name }}
									</h3>
									<span
										class="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full"
										>Active</span
									>
								</div>
								<p class="text-sm text-gray-600 mb-3">
									{{ supplier.description }}
								</p>
								<ul class="text-sm text-gray-700 space-y-1">
									<li>
										<span class="material-icons text-sm align-middle mr-1"
											>person</span
										>
										{{ supplier.contactPerson }}
									</li>
									<li>
										<span class="material-icons text-sm align-middle mr-1"
											>call</span
										>
										{{ supplier.phone }}
									</li>
									<li>
										<span class="material-icons text-sm align-middle mr-1"
											>email</span
										>
										{{ supplier.email }}
									</li>
									<li>
										<span class="material-icons text-sm align-middle mr-1"
											>location_on</span
										>
										{{ supplier.location }}
									</li>
								</ul>
							</div>
							<div class="flex justify-between items-center mt-4">
								<div v-html="renderStars(supplier.rating)"></div>
								<button class="border text-sm px-3 py-1 rounded hover:bg-gray-50">
									Visit Website
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Recent Orders -->
			<div class="bg-white p-4 rounded border shadow-sm">
				<h2 class="text-lg font-semibold mb-1">Recent Orders</h2>
				<p class="text-sm text-gray-500 mb-4">Your most recent supplier orders</p>

				<div
					v-for="order in recentOrders"
					:key="order.id"
					class="border-b py-3 last:border-0"
				>
					<div class="flex justify-between items-center">
						<div>
							<p class="font-medium text-gray-800">{{ order.supplier }}</p>
							<p class="text-xs text-gray-500">
								Order #{{ order.id }} • {{ order.date }}
							</p>
							<span
								:class="statusClass(order.status)"
								class="text-xs px-2 py-0.5 rounded-full inline-block mt-1"
							>
								{{ order.status }}
							</span>
						</div>
						<div class="text-right">
							<p class="font-semibold text-gray-800">
								${{ order.amount.toFixed(2) }}
							</p>
							<p class="text-xs text-gray-500">{{ order.items }} items</p>
						</div>
					</div>
				</div>

				<button class="w-full mt-4 text-sm text-blue-600 border-t pt-3 hover:underline">
					View All Orders
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
const suppliers = [
	{
		id: 'SUP001',
		name: 'MedPlus Supplies',
		category: 'Medical Supplies',
		contact: 'contact@medplus.com',
		rating: 5,
	},
	{
		id: 'SUP002',
		name: 'PharmaTech Inc.',
		category: 'Medications',
		contact: 'sales@pharmatech.com',
		rating: 4,
	},
	{
		id: 'SUP003',
		name: 'MedEquip Solutions',
		category: 'Equipment',
		contact: 'info@medequip.com',
		rating: 4,
	},
	{
		id: 'SUP004',
		name: 'Health Supply Co.',
		category: 'Medical Supplies',
		contact: 'orders@healthsupply.com',
		rating: 3,
	},
	{
		id: 'SUP005',
		name: 'Office Depot Medical',
		category: 'Office Supplies',
		contact: 'medical@officedepot.com',
		rating: 4,
	},
	{
		id: 'SUP006',
		name: 'Global Pharma Ltd.',
		category: 'Medications',
		contact: 'sales@globalpharma.com',
		rating: 5,
	},
	{
		id: 'SUP008',
		name: 'Lab Supplies Direct',
		category: 'Laboratory',
		contact: 'orders@labsupplies.com',
		rating: 3,
	},
]

function renderStars(rating) {
	return '★'.repeat(rating) + '<span class="text-gray-300">' + '★'.repeat(5 - rating) + '</span>'
}
const featuredSuppliers = [
	{
		name: 'MedPlus Supplies',
		description:
			'Leading provider of high-quality medical supplies and equipment for healthcare facilities.',
		contactPerson: 'Sarah Johnson',
		phone: '(555) 123-4567',
		email: 'contact@medplus.com',
		location: 'Chicago, IL',
		rating: 5,
	},
	{
		name: 'PharmaTech Inc.',
		description:
			'Specialized pharmaceutical supplier with a wide range of medications and healthcare products.',
		contactPerson: 'Michael Chen',
		phone: '(555) 987-6543',
		email: 'sales@pharmatech.com',
		location: 'Boston, MA',
		rating: 4,
	},
	{
		name: 'MedEquip Solutions',
		description:
			'Premium medical equipment provider specializing in diagnostic and treatment devices.',
		contactPerson: 'David Rodriguez',
		phone: '(555) 456-7890',
		email: 'info@medequip.com',
		location: 'San Diego, CA',
		rating: 4,
	},
	{
		name: 'Global Pharma Ltd.',
		description:
			'International pharmaceutical supplier with extensive inventory of medications and treatments.',
		contactPerson: 'Emma Wilson',
		phone: '(555) 789-0123',
		email: 'sales@globalpharma.com',
		location: 'New York, NY',
		rating: 5,
	},
]

const recentOrders = [
	{
		id: 'ORD4872',
		supplier: 'MedPlus Supplies',
		date: 'Apr 18, 2023',
		status: 'Delivered',
		amount: 1245.0,
		items: 12,
	},
	{
		id: 'ORD4865',
		supplier: 'PharmaTech Inc.',
		date: 'Apr 15, 2023',
		status: 'Shipped',
		amount: 876.5,
		items: 8,
	},
	{
		id: 'ORD4861',
		supplier: 'MedEquip Solutions',
		date: 'Apr 12, 2023',
		status: 'Processing',
		amount: 2340.75,
		items: 5,
	},
	{
		id: 'ORD4858',
		supplier: 'Health Supply Co.',
		date: 'Apr 10, 2023',
		status: 'Delivered',
		amount: 567.25,
		items: 15,
	},
]

function statusClass(status) {
	switch (status) {
		case 'Delivered':
			return 'bg-green-100 text-green-700'
		case 'Shipped':
			return 'bg-blue-100 text-blue-700'
		case 'Processing':
			return 'bg-yellow-100 text-yellow-700'
		default:
			return 'bg-gray-100 text-gray-700'
	}
}
// function renderStars(rating) {
// 	return (
// 		'<span class="text-yellow-500">' +
// 		'★'.repeat(rating) +
// 		'</span><span class="text-gray-300">' +
// 		'★'.repeat(5 - rating) +
// 		'</span>'
// 	)
// }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
</style>
